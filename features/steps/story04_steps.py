# Step Definitions for Story 4: Remove a task from a course
# Created by Helen Lin

from behave import *
import requests

# ------------- Helper functions ---------------------------
def cleanup_tasks(context):
   #delete any created tasks
    if (hasattr(context, 'task_ID')):
        requests.delete("http://localhost:4567/todos/" + context.task_ID)
    if (hasattr(context, 'course_ID')):
        requests.delete("http://localhost:4567/projects/" + context.course_ID)
    return

# ------ scenario 1 - remove existing task ----------
@given(u'this task is already added to the course')
def step_impl(context):
    requests.post("http://localhost:4567/todos/"+ context.task_ID + '/tasksof', json={"id": context.course_ID})

@when(u'I remove the task from this course')
def step_impl(context):
    context.response = requests.delete("http://localhost:4567/projects/"+ context.course_ID + "/tasks/" + context.task_ID)

@then(u'the course should not have the task anymore')
def step_impl(context):
    assert(context.response.status_code == 200)
    todos = requests.get("http://localhost:4567/projects/"+ context.course_ID + "/tasks").json()["todos"]
    found = False
    for i in range(len(todos)):
        if (todos[i]["id"] == context.task_ID):
            found = True
    assert(found == False)

    cleanup_tasks(context)

# ------------- scenario 2 - mark task as done and remove from list ----------------------

# all steps previously defined and in other stories

# ---------------------- scenario 3 - invalid course ---------------------------

# all steps defined previously and in story01 and story10# all steps previously defined and in other stories