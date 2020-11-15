from behave import *
# NOTE: conversion from feature ie: "Given I have three precreated priority levels in my system" IS A MACRO REGISTER W
import requests
import json

def create_priorities(context, priorities):
    endpoint = "projects/1/tasks"
    url = context.url + endpoint
    for idx, priority in enumerate(priorities):
        title = "project task: {}".format(idx)
        description = "Priority: {} a good description".format(priority)
        params = {"title": title, "description": description}

        body = {'data': json.dumps(params)}
        response = requests.post(url, **body).json()
        context.created_ids[endpoint].append(response["id"])

        # post projects/id/tasks creates a todo also that we need to delete
        context.created_ids['todos'].append(response["id"])
        print('response to post projects/1/tasks: {}'.format(response))



# ===================== normal flow ============================================
@given('I have three precreated priority levels in my system')
def step_impl(context):
    priorities = [ 'HIGH', 'MEDIUM', 'LOW' ]
    create_priorities(context, priorities)


@given('I have an existing valid task with title {title} and priority {oldPriority}')
def step_impl(context, title, oldPriority):
    endpoint = "projects/1/tasks"
    url = context.url + endpoint
    description = "Priority: {} a good description".format(oldPriority)
    params = {"title": title, "description": description}

    body = {'data': json.dumps(params)}
    response = requests.post(url, **body).json()
    # print(f'first given response: {response}')
    context.created_ids[endpoint].append(response["id"])
    context.created_ids['todos'].append(response["id"])
    # print(f'response ID: {response["id"]}')


@given('the new priority {newPriority} is not the same as the old priority {oldPriority}')
def step_impl(context, newPriority, oldPriority):
    pass

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
