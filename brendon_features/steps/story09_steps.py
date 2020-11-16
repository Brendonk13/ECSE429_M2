from behave import *
# NOTE: conversion from feature ie: "Given I have three precreated priority levels in my system" IS A MACRO REGISTER W
import requests
import re
import logging
import sys
sys.path.append('../helpers')
from helpers.story_9 import Task, create_task, setup_context_url_stuff, get_todo_id, category_id_from_priority



def create_todo_with_priority(context, priority, title):
    description = '{} Priority Tasks'.format(priority)

    priority_category_id = category_id_from_priority(context, priority)
    endpoint = 'categories/{}/todos'.format(priority_category_id)
    setup_context_url_stuff(context, endpoint)

    task = create_task(context, title, description, priority)

    # add resources that need to be deleted to restore state
    response = requests.get(context.base_url + 'categories').json()
    todo_id = get_todo_id(response, priority_category_id)
    # todo_id = task.response['id']
    endpoint = 'categories/{}/todos'.format(priority_category_id)
    # context.created_ids[endpoint].append(task)
    # context.prev_task = task
    return task


def delete_todo_with_priority(context, priority, todo_id):
    '''
        to do this we need to delete 2 resources:
        categories/category_id/todos/todo_id
        todos/todo_id
    '''
    category_id = category_id_from_priority(context, priority)
    # logging.info(f'DELETE PRIORITY: {priority}, category ID: {category_id}')
    # response = requests.get(context.base_url + 'categories').json()
    # todo_id = get_todo_id(response, category_id)
    # todo_id = 

    endpoint = 'categories/{}/todos/{}'.format(category_id, todo_id)

    setup_context_url_stuff(context, endpoint)
    logging.info(f'DELETE: {context.url}')
    response = requests.delete(context.url)
    logging.info(response)
    assert response.ok

    url = context.base_url + 'todos/{}'.format(todo_id)
    logging.info(f'DELETE: {url}')
    response = requests.delete(url)
    logging.info(response)
    assert response.ok
    logging.info('')
# ===================== HELPERS ===================================================






# ===================== normal flow ============================================
@given('I have three precreated priority levels in my system')
def step_impl(context):
    # this step is common to story 9 and is therefor handled in:
    # environment.py/before_feature function which call setup_story9_environment()
    pass


@given('I have an existing valid task with title {title} and priority {oldPriority}')
def step_impl(context, title, oldPriority):
    # ============== add todo to category: oldPriority =========================
    category_id = category_id_from_priority(context, oldPriority)
    logging.info(f'OLD PRIORITY: {oldPriority}, category ID: {category_id}')
    context.prev_task = create_todo_with_priority(context, oldPriority, title)


@given('the new priority {newPriority} is not the same as the old priority {oldPriority}')
def step_impl(context, newPriority, oldPriority):
    # search through description of created_ids[-1]
    task = context.prev_task
    assert (oldPriority == task.priority) and (newPriority != task.priority)


@when('I add the task to the category {newPriority}')
def step_impl(context, newPriority):
    prev_task = context.prev_task
    delete_todo_with_priority(context, prev_task.priority, prev_task.created_id)

    # change the prev_task to the new priority
    priority_category_id = category_id_from_priority(context, newPriority)
    endpoint = 'categories/{}/todos'.format(priority_category_id)
    setup_context_url_stuff(context, endpoint)
    # assign this prev_task
    logging.info(f'url to create_task: {context.url}')
    changed_task = create_task(context, prev_task.title, prev_task.description, newPriority)
    context.prev_task = changed_task

    logging.info('just tried to post the NEW TODO with NEW PRIORITY')
    logging.info('')

    context.created_ids['todos'].append(changed_task)


@then('the task should have category {newPriority}')
def step_impl(context, newPriority):
    prev_task = context.prev_task
    url = context.url
    logging.info(f'Then: url we get from for verification: {url}')

    response = requests.get(url)
    assert response.ok

    for todo in response.json()['todos']:
        if todo['id'] == prev_task.created_id:
            response_body = todo
            break

    # logging.info(f'full response body: {response_body}')
    # response_body = response_body[-1]
    logging.info(f'the response body: {response_body}')
    logging.info(f'the stored response: {prev_task.response}')
    assert all(response_body[key] == prev_task.response[key] for key in response_body)
    context.prev_task = None
    context.prev_task = ''
# ===================== normal flow ============================================



# # ===================== alternate flow =========================================
# @given('Given I have three precreated priority levels in my system')
# def step_impl(context):
#     # this step is common to story 9 and is therefor handled in:
#     # environment.py/before_feature function which call setup_story9_environment()
#     pass

# @given('I have an existing valid task with title {title} and priority {oldPriority}')
# def step_impl(context):
#     context.prev_task = create_todo_with_priority(context, oldPriority, title)

@given('the new priority {newPriority} is the same as the old priority {oldPriority}')
def step_impl(context, newPriority, oldPriority):
    task = context.prev_task
    assert (oldPriority == newPriority) and (newPriority == task.priority)

# @when('I add the task to the category <newPriority>')
# def step_impl(context):
#     pass

# @then('the task should have category <newPriority>')
# def step_impl(context):
#     pass

# ===================== alternate flow =========================================
