# Step Definitions for Story 1: Categorize tasks by priority (story01_categorize_tasks_priority.feature)

from behave import *
import requests

# ------------- Helper functions ---------------------------
def create_todo(title):
    # creates a new task and returns new todo's id
    task = requests.post("http://localhost:4567/todos", json={"title": title})
    return task.json()["id"]

def create_category(category_name):
    #create a new category and returns the ID of this category
    response = requests.post("http://localhost:4567/categories", json={"title": category_name})
    return response.json()["id"]

def get_priority_id(context, priority):
    # return the id of the priority type
    if (priority == 'HIGH'):
        p = context.HIGH_id
    elif (priority == 'MEDIUM'):
        p = context.MEDIUM_id
    elif (priority == 'LOW'):
        p = context.LOW_id
    else:
        p = -1
    return p

def cleanup_tasks_priority(context):
    # cleanup for this story entails deleting the 3 created categories, and deleting any created tasks
    if (context.task_ID):
        requests.delete("http://localhost:4567/todos/" + context.task_ID)
    if (context.HIGH_id):
        requests.delete("http://localhost:4567/categories/" + context.HIGH_id)
    if (context.MEDIUM_id):
        requests.delete("http://localhost:4567/categories/" + context.MEDIUM_id)
    if (context.LOW_id):
        requests.delete("http://localhost:4567/categories/" + context.LOW_id)
    return

# ------ scenario 1 - valid new task with priority ----------
@given(u'I have three precreated priority levels in my system')
def step_impl(context):
    context.HIGH_id = create_category('HIGH')
    context.MEDIUM_id = create_category('MEDIUM')
    context.LOW_id = create_category('LOW')
     
@when(u'I create a new task with title {title} and priority level {priority}')
def step_impl(context, title, priority):
    context.task_ID = create_todo(title) # create new task

    # add to category
    p = get_priority_id(context,priority)
    context.response = requests.post("http://localhost:4567/todos/"+ context.task_ID + '/categories', json={"id": p})

@then(u'the task should have category {priority}')
def step_impl(context, priority):
    # check that category was added correctly
    assert(context.response.status_code == 201)
    response = requests.get("http://localhost:4567/todos/"+ context.task_ID + '/categories').json()
    assert(priority == response["categories"][0]["title"])

    #clean up: delete categories and tasks created
    cleanup_tasks_priority(context)

# ------------- scenario 2 - valid existing task with priority ----------------------
@given(u'I have an existing valid task with title {title}')
def step_impl(context, title):
    context.task_ID = create_todo(title) # create new task

@when(u'I add the task to the category {priority}')
def step_impl(context, priority):
    p = get_priority_id(context,priority)
    context.response = requests.post("http://localhost:4567/todos/"+ context.task_ID + '/categories', json={"id": p})


# ---------------------- scenario 3 - invalid priority ---------------------------
@given(u'{priority} is not the name of an existing category')
def step_impl(context, priority):
    categories = requests.get("http://localhost:4567/categories").json()['categories']
    for i in range(len(categories)):
        assert(priority != categories[i]['title'])

@then(u'there should be an error returned from the system')
def step_impl(context):
    assert(context.response.status_code == 404)

@then(u'the task should not have category {priority}')
def step_impl(context, priority):
    response = requests.get("http://localhost:4567/todos/"+ context.task_ID + '/categories').json()
    categories = response["categories"]
    if (categories):
        for i in range (len(categories)):
            assert(priority != categories[i]["title"])

    #clean up: delete categories and tasks created
    cleanup_tasks_priority(context)