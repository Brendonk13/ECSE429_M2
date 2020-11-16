# Step Definitions for Story 10: Change task descriptions

from behave import *
import requests

# ----Helper functions -----
def create_todo(title, description):
    # creates a new task with description and returns new todo's id
    if (description != ""):
        task = requests.post("http://localhost:4567/todos", json={"title": title, "description": description})
    else:
        task = requests.post("http://localhost:4567/todos", json={"title": title})
    return task.json()["id"]

def cleanup_descr(context):
    # cleanup for this story entails any created tasks
    if (context.task_ID):
        requests.delete("http://localhost:4567/todos/" + context.task_ID)
    return

# -------- scenario 1 - valid update description -----------
@given(u'^I have an existing task with title {title} and description {oldDescription}&')
def step_impl(context, title, oldDescription):
    context.task_ID = create_todo(title, oldDescription) # create new task
     
@given(u'the new description {newDescription} is not the same as the old description {oldDescription}')
def step_impl(context, newDescription, oldDescription):
    assert(newDescription != oldDescription)

@when(u'I update the description to {description}')
def step_impl(context, description):
    context.response = requests.post("http://localhost:4567/todos/"+ context.task_ID, json={"description": description})

@then(u'the task should have description {description}')
def step_impl(context, description):
    assert(context.response.status_code == 200)
    response = requests.get("http://localhost:4567/todos/"+ context.task_ID).json()
    assert(response["todos"][0]["description"] == description)

    #cleanup
    cleanup_descr(context)

# ------- scenario 2 - valid existing task with no previous description ---------------
@given(u'I have a valid task with title {title} and no description')
def step_impl(context, title):
     context.task_ID = create_todo(title, "") # create new task w no descr
    
# ------ scenario 3 - update valid task with same description -----------------
@given(u'the new description {newDescription} is the same as the old description {oldDescription}')
def step_impl(context, newDescription, oldDescription):
    assert(newDescription == oldDescription)

# scenario 4 - invalid task
@given(u'there is no task in the system with id {id}')
def step_impl(context, id):
    context.task_ID = id
    resp = requests.get("http://localhost:4567/todos/" + id)
    assert(resp.status_code == 404)

# Note: THEN step def defined in story01's step defs