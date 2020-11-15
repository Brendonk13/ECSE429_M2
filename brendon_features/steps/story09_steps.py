from behave import *
# NOTE: conversion from feature ie: "Given I have three precreated priority levels in my system" IS A MACRO REGISTER W
import requests
import json
import re

class Task:
    def __init__(self, title, priority, ID, response):
        self.title = title
        # self.description = description
        self.priority = priority
        self.created_id = ID
        self.response = response

    def __add__(self, other):
        # need cuz used in "after_scenario" for this feature
        return self.created_id + other

    def __radd__(self, other):
        return other + self.created_id

    def __repr__(self):
        return self.created_id



def create_task(context, title, description, priority):
    # create a task object storing basic response information
    # and return the ID of the object just created
    params = {"title": title, "description": description}

    body = {'data': json.dumps(params)}
    response = requests.post(context.url, **body).json()
    print(f'response to post {context.endpoint}: {response}')

    ID = response["id"]
    task = Task(title, priority, ID, response)
    context.created_ids[context.endpoint].append(task)
    return task


def setup_environment(context, priorities):
    # create 3 priority levels by creating 3 tasks with different priorities
    # context.init_env = []
    for idx, priority in enumerate(priorities):
        title = "Priority: {}".format(priority)
        description = "{} Priority Tasks".format(priority)

        task = create_task(context, title, description, priority)
        # context.init_env.append(task)
        # post projects/id/tasks creates a todo also that we need to delete
        context.created_ids['categories'].append(task.created_id)
# ===================== HELPERS ===================================================






# ===================== normal flow ============================================
@given('I have three precreated priority levels in my system')
def step_impl(context):
    context.endpoint =  "todos/1/categories"
    context.url = context.base_url + context.endpoint
    priorities = [ 'HIGH', 'MEDIUM', 'LOW' ]
    setup_environment(context, priorities)


@given('I have an existing valid task with title {title} and priority {oldPriority}')
def step_impl(context, title, oldPriority):
    todo_id = 1
    context.endpoint = "projects/{}/tasks".format(todo_id)
    context.url = context.base_url + context.endpoint
    description = "References Todo id:{}".format(todo_id)

    task = create_task(context, title, description, oldPriority)
    # side effect of creating task is a todo is created
    context.created_ids['todos'].append(task.created_id)
    # print(f'response ID: {response["id"]}')


@given('the new priority {newPriority} is not the same as the old priority {oldPriority}')
def step_impl(context, newPriority, oldPriority):
    # search through description of created_ids[-1]
    task = context.created_ids[context.endpoint][-1]
    assert newPriority != task.priority


@when('I add the task to the category {newPriority}')
def step_impl(context, newPriority):
    pass



@then('the task should have category {newPriority}')
def step_impl(context, newPriority):
    pass

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
