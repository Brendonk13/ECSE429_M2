from behave import *
import requests
import logging


@given('The class {class_id} exists')
def step_impl(context, class_id):
    obj_name = 'projects'
    logging.info('before checking project exists')
    response = requests.get(context.base_url + obj_name)
    response_body = response.json()[obj_name]
    logging.info('after checking project exists, response: {}'.format(response_body))

    found_project = any(
            project['id'] == class_id
            for project in response_body
    )

    assert found_project
    assert response.ok


@given('The class has an incomplete task with title {title}')
def step_impl(context, title):
    obj_name = 'projects/1/tasks'
    json = {'title': title, 'doneStatus': False}
    logging.info('before creating incomplete task with params: {}'.format(json))
    response = requests.post(context.base_url + obj_name, json=json)

    logging.info('after post request, response: {}'.format(response))
    response_body = response.json()
    logging.info('response_body: {}'.format(response_body))
    assert response.ok

    created_id = response_body['id']
    logging.info('incomplete task created_id: {}'.format(created_id))

    context.prev_created_id = created_id
    # this obj will be deleted after the scenario
    context.created_ids[obj_name].append(created_id)
    context.created_ids['todos'].append(created_id)



@when('I view all incomplete tasks')
def step_impl(context):
    response = requests.get(context.base_url + 'todos')
    context.incomplete_tasks = response.json()['todos']
    logging.info('all incomplete tasks: {}'.format(context.incomplete_tasks))
    assert response.ok


@then('The incomplete task with title {title} should exist and be marked incomplete')
def step_impl(context, title):
    logging.info('')
    logging.info('')
    for task in context.incomplete_tasks:
        if all((
                context.prev_created_id == task['id'],
                title == task['title'],
                )):
            logging.info('found the incomplete task')
            assert task['doneStatus'] == 'false'
            logging.info('doneStatus is false!')
            return

    # occurs if we don't find task and hence don't return
    assert False
