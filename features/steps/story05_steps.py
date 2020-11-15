
from behave import *
import requests
import unittest
"""
Step Definitions for story05_create_todo_list
"""


@when('user does a post request to the server with {title}')
def step_imp(context, title):

    context.response = requests.post("http://localhost:4567/projects", json={"title": title})
    assert context.response.status_code == 201
    response_body = context.response.json()
    context.new_id = response_body["id"]



@then('class with the name {title} is created')
def step_imp(context, title):

    context.response = requests.get("http://localhost:4567/projects" + "/" + context.new_id)
    assert context.response.status_code == 200
    context.response = requests.delete("http://localhost:4567/projects" + "/" + context.new_id)

@when('user does a post request with {title} and  and {description}')
def step_imp(context,title,description):
    classname = {"title": title, "description":description}
    context.response_class2 = requests.post("http://localhost:4567/projects", json=classname )
    assert context.response_class2.status_code == 201
    response_body = context.response_class2.json()
    context.new_id2 = response_body["id"]


@then('class with {title} and {description} is created')
def step_imp(context,title,description):
    context.response = requests.get("http://localhost:4567/projects" + "/" + context.new_id2)
    assert context.response.status_code == 200
    context.response = requests.delete("http://localhost:4567/projects" + "/" + context.new_id2)



@when('user does a bad post request to the server with {title} and {id}')
def step_imp(context,title,id):
    context.className = {"title":title, "id":id}
    context.response_class = requests.post("http://localhost:4567/projects", json=context.className )
    assert context.response_class.status_code == 400

@then('"Error 400 Bad Request" will happen for that {title} and {id}')
def step_imp(context,title,id):
    context.className = {"title": title, "id": id}
    context.response_class = requests.get("http://localhost:4567/projects" + "/" + id)
    assert context.response_class.status_code == 404


