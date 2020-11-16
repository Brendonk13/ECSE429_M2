from behave import *
# NOTE: conversion from feature ie: "Given I have three precreated priority levels in my system" IS A MACRO REGISTER W
import requests
import json
import re
import logging



class Task:
    def __init__(self, title, priority, ID, response, description, url):
        self.title = title
        # self.description = description
        self.priority = priority
        self.created_id = ID
        self.response = response
        self.description = description
        self.url = url

    def __add__(self, other):
        # need cuz used in "after_scenario" for this feature
        return self.created_id + other

    def __radd__(self, other):
        return other + self.created_id

    def __repr__(self):
        return self.created_id



# default None for setup_environment fxn
# it doesn't actually create a task but does everything else
def create_task(context, title, description, priority, todo_id=None):
    # create a task object storing basic response information
    # and return the ID of the object just created
    params = {"title": title, "description": description}
    body = {'data': json.dumps(params)}
    response = requests.post(context.url, **body)
    assert response.ok
    response_body = response.json()
    logging.info(f'response to post {context.endpoint}: {response_body}')

    ID = response_body["id"]
    task = Task(title, priority, ID, response_body, description, context.url)
    return task


def category_id_from_priority(context, priority):
    for category in context.init_env:
        if category.priority == priority:
            return category.created_id


def get_todo_id(response, obj_ID):
    for category in response['categories']:
        if obj_ID == category['id']:
            return category['todos'][-1]['id']


def setup_context_url_stuff(context, endpoint):
    context.endpoint = endpoint
    context.url = context.base_url + endpoint


def setup_environment(context, priorities):
    # create 3 priority levels by creating 3 tasks with different priorities
    context.init_env = []
    for idx, priority in enumerate(priorities):
        title = "Priority: {}".format(priority)
        description = "{} Priority Tasks".format(priority)

        task = create_task(context, title, description, priority, None)
        context.created_ids[context.endpoint].append(task)
        context.init_env.append(task)
        # print(priority)
        # post projects/id/tasks creates a todo also that we need to delete
        # context.created_ids[context.endpoint].append(task.created_id)

# ===================== HELPERS ===================================================






# ===================== normal flow ============================================
@given('I have three precreated priority levels in my system')
def step_impl(context):
    setup_context_url_stuff(context, 'categories')
    priorities = [ 'HIGH', 'MEDIUM', 'LOW' ]
    setup_environment(context, priorities)


@given('I have an existing valid task with title {title} and priority {oldPriority}')
def step_impl(context, title, oldPriority):
    # ============== add todo to category: oldPriority =========================
    priority_category_id = category_id_from_priority(context, oldPriority)
    endpoint = 'categories/{}/todos'.format(priority_category_id)
    setup_context_url_stuff(context, endpoint)
    description = '{} Priority Tasks'.format(oldPriority)

    task = create_task(context, title, description, oldPriority)
    context.prev_task = task


@given('the new priority {newPriority} is not the same as the old priority {oldPriority}')
def step_impl(context, newPriority, oldPriority):
    # search through description of created_ids[-1]
    task = context.prev_task
    assert (oldPriority == task.priority) and newPriority != task.priority


@when('I add the task to the category {newPriority}')
def step_impl(context, newPriority):

    # first remove the task from its associations with its oldPriority
    prev_task = context.prev_task
    priority_category_id = category_id_from_priority(context, prev_task.priority)
    response = requests.get(context.base_url + 'categories').json()
    todo_id = get_todo_id(response, priority_category_id)

    # delete this todo from previous category
    url = 'categories/{}/todos/{}'.format(priority_category_id, todo_id)
    setup_context_url_stuff(context, url)
    logging.info(f'DELETE: {context.url}')
    response = requests.delete(context.url)
    assert response.ok


    url = context.base_url + 'todos/{}'.format(todo_id)
    logging.info(f'DELETE: {url}')
    response = requests.delete(url)
    assert response.ok
    logging.info('')
    # print()
    # print()


    # change the prev_task to the new priority
    endpoint = 'categories/{}/todos'.format(priority_category_id)
    setup_context_url_stuff(context, endpoint)
    # assign this prev_task
    logging.info(f'url to create_task: {context.url}')
    changed_task = create_task(context, prev_task.title, prev_task.description, newPriority)
    logging.info('just tried to post the NEW TODO with NEW PRIORITY')
    logging.info('')
    # print()
    # print()

    context.created_ids['todos'].append(changed_task)
    # context.created_ids['todos'].append(new_todo_id)
    context.prev_task = changed_task




@then('the task should have category {newPriority}')
def step_impl(context, newPriority):
    prev_task = context.prev_task
    # url = prev_task.url
    # print(f'the context url is: {context.url}')
    url = context.url # + '/' + prev_task.created_id
    logging.info(f'Then: url we get from for verification: {url}')
    # print()
    # print()
    # print()
    response = requests.get(url)
    assert response.ok
    response_body = response.json()['todos'][0]
    logging.info(f'the response body: {response_body}')
    logging.info(f'the stored response: {prev_task.response}')
    # print()
    # print()
    # print()
    assert all(response_body[key] == prev_task.response[key] for key in response_body)


    # endpoint = '

# ===================== normal flow ============================================



# # ===================== alternate flow =========================================
# @given('Given I have three precreated priority levels in my system')
# def step_impl(context):
#     pass

# # @given('I have an existing valid task with title <title> and priority <oldPriority>')
# # def step_impl(context):
# #     pass

# @given('the new priority <newPriority> is the same as the old priority <oldPriority>')
# def step_impl(context):
#     pass

# @when('I add the task to the category <newPriority>')
# def step_impl(context):
#     pass

# # @then('the task should have category <newPriority>')
# # def step_impl(context):
# #     pass

# # ===================== alternate flow =========================================
