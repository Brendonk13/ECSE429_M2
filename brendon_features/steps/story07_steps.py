from behave import *
import requests
import logging
from helpers.story_9 import get_done_status


# ===================== helpers ================================================


def get_all_todos(context):
    return requests.get(context.base_url + 'todos')


def get_projects(context):
    obj_name = 'projects'
    logging.info('before checking project exists')
    response = requests.get(context.base_url + obj_name)
    response_body = response.json()[obj_name]
    logging.info('after checking project exists, response: {}'.format(response_body))
    assert response.ok

    return response_body


def value_in_response(searched_for_value, response_body, key=None):
    return any(
        obj[key] == searched_for_value
        for obj
        in response_body
    )


def project_exists(project_id, projects):
    return value_in_response(project_id, projects, key='id')
# ===================== helpers ================================================





@given('The class {project_id} exists')
def step_impl(context, project_id):
    assert project_exists(project_id, get_projects(context))


@given('The class has an {doneStatus} task with title {title}')
def step_impl(context, doneStatus, title):
    obj_name = 'projects/1/tasks'
    done_status = get_done_status(doneStatus)

    json = {'title': title, 'doneStatus': done_status}
    logging.info('before creating {} task with params: {}'.format(done_status, json))
    response = requests.post(context.base_url + obj_name, json=json)

    logging.info('after post request, response: {}'.format(response))
    response_body = response.json()
    logging.info('response_body: {}'.format(response_body))
    assert response.ok

    created_id = response_body['id']
    logging.info('{} task created_id: {}'.format(done_status, created_id))

    context.prev_created_id = created_id
    # this obj will be deleted after the scenario
    context.created_ids[obj_name].append(created_id)
    context.created_ids['todos'].append(created_id)


@when('I view all {doneStatus} tasks')
def step_impl(context, doneStatus):
    done_status = get_done_status(doneStatus)
    response = get_all_todos(context)
    context.tasks = response.json()['todos']
    logging.info('all {} tasks: {}'.format(done_status, context.tasks))
    assert response.ok


@then('The task with title {title} will be present and be marked {doneStatus}')
def step_impl(context, title, doneStatus):
    done_status = get_done_status(doneStatus)
    logging.info('')
    logging.info('')
    for task in context.tasks:
        if all((
                context.prev_created_id == task['id'],
                title == task['title'],
                )):
            logging.info('found the {} task'.format(done_status))
            assert task['doneStatus'] == doneStatus
            logging.info('doneStatus is {}!'.format(done_status))
            return

    # occurs if we don't find task and hence don't return
    assert False


@then('The task with title {title} will be not present')
def step_impl(context, title):
    assert not value_in_response(title, context.tasks, key='title')
