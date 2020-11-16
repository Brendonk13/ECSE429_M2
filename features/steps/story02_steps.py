# Step Definitions for Story 2: Add a task to a course
# Created by Helen Lin

from behave import *
import requests

# ------------- Helper functions ---------------------------
def create_todo(title):
    # creates a new task and returns new todo's id
    task = requests.post("http://localhost:4567/todos", json={"title": title})
    return task.json()["id"]

def create_course(course_name):
    #create a new course as a project and returns the ID
    response = requests.post("http://localhost:4567/projects", json={"title": course_name})
    return response.json()["id"]

def cleanup_tasks_course(context):
    # cleanup for this story entails deleting the 3 created categories, and deleting any created tasks
    if (hasattr(context, 'task_ID')):
        requests.delete("http://localhost:4567/todos/" + context.task_ID)
    if (hasattr(context, 'course_ID')):
        requests.delete("http://localhost:4567/projects/" + context.course_ID)
    return

# ------ scenario 1 - add task to a course ----------
@given(u'I have an existing course {course}')
def step_impl(context, course):
    context.course_ID = create_course(course) # create new course

# existing valid task step def in story01

@when(u'I add the task to the course')
def step_impl(context):
    context.response = requests.post("http://localhost:4567/todos/"+ context.task_ID + '/tasksof', json={"id": context.course_ID})

@then(u'the task should be a task of {course}')
def step_impl(context, course):
    # check that course was added correctly
    assert(context.response.status_code == 201)
    response = requests.get("http://localhost:4567/todos/"+ context.task_ID + '/tasksof').json()
    assert(course == response["projects"][0]["title"])

@then(u'the course should have the task with title {title}')
def step_impl(context, title):
    # check that task was added correctly
    tasks = requests.get("http://localhost:4567/projects/"+ context.course_ID + "/tasks").json()["todos"]
    found = False
    for i in range(len(tasks)):
        if (tasks[i]["title"] == title and tasks[i]["id"]==context.task_ID):
            found = True
    assert(found, True)

    #clean up: delete categories and tasks created
    cleanup_tasks_course(context)

# ------------- scenario 2 - add a new task to a course ----------------------
@when(u'I create a new task with title {title}')
def step_impl(context, title):
    context.task_ID = create_todo(title) # create new task
# other steps previously defined

# ---------------------- scenario 3 - invalid course ---------------------------
@given(u'I do not have existing course {course}')
def step_impl(context, course):
    projects = requests.get("http://localhost:4567/projects").json()['projects']
    for i in range(len(projects)):
        assert(course != projects[i]['title'])
    context.course_ID = '-1' #invalid course id placeholder
# other steps defined previously or in story01

# ---------------------- scenario 4 - invalid task---------------------------

# all steps defined previously or in story01 and story10