from behave import *
import requests
import logging
from helpers.story_9 import Task, create_task, setup_context_url_stuff, todo_id_from_response, category_id_from_priority, all_categories_response, CategoryDoesNotExist, create_todo_with_priority, delete_todo_with_priority, get_done_status


def create_project(context):
    obj_name = 'projects'
    response = requests.post(context.base_url + obj_name)
    logging.info(f'the response: {response}')
    logging.info(f'the response_body: {response.json()}')
    response_body = response.json()
    context.created_ids[obj_name].append(response_body['id'])

    assert response.ok
    return response_body, response_body['id']


@given('I am currently enrolled in two classes')
def step_impl(context):
    context.created_projects = []
    context.created_projects.append(create_project(context))
    context.created_projects.append(create_project(context))
    logging.info('created classes: {}'.format(context.created_projects))


@given('Both classes have a task with title {title} and priority {priority}')
def step_impl(context, title, priority):
    for project, ID in context.created_projects:
        # context.created_ids['projects'].append(ID)
        category_id = category_id_from_priority(context, priority)
        task = create_todo_with_priority(context, priority, title)
        # context.created_ids['todos'].append(task)
        todo_id = task.created_id

        endpoint = f'projects/{ID}/tasks'
        setup_context_url_stuff(context, endpoint)
        description = f'References todo: {todo_id}'
        json = {'title' : title, 'description': description}
        response = requests.post(context.url, json = json)
        logging.info(f'request to: {endpoint} response_body: {response.json()}')
        response_body = response.json()

        assert response.ok
        context.created_ids['todos'].append(response_body['id'])
        delete_todo_with_priority(context, priority, todo_id)
        context.must_delete_todos = []
        context.must_delete_todos.append((priority, todo_id))


@when('When I view all {doneStatus} {priority} priority tasks')
def step_impl(context, doneStatus, priority):
    done_status = get_done_status(doneStatus)
    category_id = category_id_from_priority(priority)

    response = requests.get(context.base_url + 'categories/{category_id}/todos')
    logging.info('response body for all {priority} priority todos: {response.json()}')
    response_body = response.json()
    assert response.ok


@then('The {priority} priority task with title {title} will be present and be marked {doneStatus}')
def step_impl(context, priority, title):

    for (_priority, todo_id) in context.must_delete_todos:
        delete_todo_with_priority(context, _priority, todo_id)
    # pass


