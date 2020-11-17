from behave import *
# NOTE: conversion from feature ie: "Given I have three precreated priority levels in my system" IS A MACRO REGISTER W
import requests
import logging
from helpers.story_9 import Task, create_task, setup_context_url_stuff, todo_id_from_response, category_id_from_priority, all_categories_response, CategoryDoesNotExist, create_todo_with_priority, delete_todo_with_priority




# ===================== normal flow ============================================
@given('Three priority levels already exist in my system')
def step_impl(context):
    # this step is common to story 9 and is therefor handled in:
    # environment.py/before_feature function which call setup_story9_environment()
    pass


@given('There exists a task with title {title} and priority {oldPriority}')
def step_impl(context, title, oldPriority):
    # add todo to category: oldPriority
    category_id = category_id_from_priority(context, oldPriority)
    logging.info(f'OLD PRIORITY: {oldPriority}, category ID: {category_id}')
    context.prev_task = create_todo_with_priority(context, oldPriority, title)


@given('The new priority {newPriority} is different from the old priority {oldPriority}')
def step_impl(context, newPriority, oldPriority):
    # search through description of created_ids
    task = context.prev_task
    assert (oldPriority == task.priority) and (newPriority != task.priority)


@when('I add the relevant task to the category {newPriority}')
def step_impl(context, newPriority):
    prev_task = context.prev_task
    # delete this todo from its previous category to preserve state.
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


@then('The task should now have category {newPriority}')
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
# ===================== normal flow ============================================




# # ===================== alternate flow =========================================
@given('The new priority {newPriority} is the same as the old priority {oldPriority}')
def step_impl(context, newPriority, oldPriority):
    task = context.prev_task
    assert (oldPriority == newPriority) and (newPriority == task.priority)

# other parts of this flow are done in normal flow section

# ===================== alternate flow =========================================




# ===================== error flow =============================================

@given('the new priority for this task: {newPriority} does not exist')
def step_impl(context, newPriority):
    response = all_categories_response(context)

    logging.info('before assert all in error flow showing that newPriority: {} d.n exist'.format(newPriority))
    logging.info(f'response: {response}')
    # priorities are categories with titles of format: 'Priority: {}'.format('HIGH')
    # for thing in response['categories']:
    #     logging.info(f'iterating ..., value: {thing}')
    assert all(
        'Priority: ' + newPriority != category['title']
        for category in response
    )
    logging.info('after assert all')




@when('I add the task to the non-existant category {newPriority}')
def step_impl(context, newPriority):
    prev_task = context.prev_task
    json = {'title' : prev_task.title, 'description' : prev_task.description}
    try:
        category_id = category_id_from_priority(context, newPriority, search_all_priorities=True)
        # Fail the test if error not raised
        # response = requests.post(prev_task.url, json=json)
        assert False

    except CategoryDoesNotExist:
        assert True


@then('task should not be added to the category {newPriority}')
def step_impl(context, newPriority):
    formatted_priority = 'Priority: ' + newPriority
    for category in all_categories_response(context):
        if formatted_priority == category['description']:
            assert False
    assert True

    # cleanup created id in second @given
    prev_task = context.prev_task
    delete_todo_with_priority(context, prev_task.priority, prev_task.created_id)


# ===================== error flow =============================================
