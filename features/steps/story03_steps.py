# Step Definitions for Story 3: Mark a task as done
# Created by Helen Lin

from behave import *
import requests

# ------------- Helper functions ---------------------------
def cleanup_tasks(context):
   #delete any created tasks
    if (hasattr(context, 'task_ID')):
        requests.delete("http://localhost:4567/todos/" + context.task_ID)
    return

# ------ scenario 1 - mark existing task as done ----------
@when(u'I mark the task as done')
def step_impl(context):
    context.response = requests.post("http://localhost:4567/todos/"+ context.task_ID, json={"doneStatus": True})

@then(u'the task should be marked as done')
def step_impl(context):
    assert(context.response.status_code == 200)
    response = requests.get("http://localhost:4567/todos/"+ context.task_ID).json()
    assert(response["todos"][0]["doneStatus"] == 'true')

    cleanup_tasks(context)

# ------------- scenario 2 - mark a new task as done ----------------------

# all steps previously defined and in story01

# ---------------------- scenario 3 - invalid task ---------------------------

# all steps defined previously and in story01 and story10