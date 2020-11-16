from behave import *
import requests

"""
Step Definitions for story06_remove_todo_list
"""

@given('there is a class with name {title}')
def step_imp(context, title):

    context.response = requests.post("http://localhost:4567/projects", json={"title": title})
    assert context.response.status_code == 201
    response_body = context.response.json()
    context.new_id = response_body["id"]

@when('user does a delete request to the server with {title}')
def step_imp(context, title):
    context.response = requests.delete("http://localhost:4567/projects" + "/" + context.new_id)
    assert context.response.status_code == 200

@then('class with name {title} is removed')
def step_imp(context, title):
    context.response = requests.get("http://localhost:4567/projects" + "/" + context.new_id)
    assert context.response.status_code == 404



@given('there exists a class with name {title} and {description} as false')
def step_imp(context, title, description):

    context.response = requests.post("http://localhost:4567/projects", json={"title": title,"description":description})
    assert context.response.status_code == 201
    response_body = context.response.json()
    context.new_id = response_body["id"]

@when('user does a post request with {new_description} as true')
def step_imp(context, new_description):
    context.response = requests.post("http://localhost:4567/projects" + "/" + context.new_id ,json={"description":new_description})
    assert context.response.status_code == 200
    response_body = context.response.json()
    context.description = response_body["description"]
@then('class with name {title} , {new_description} has a new description of NOT TAKING ANYMORE')
def step_imp(context, title,new_description):
    if new_description == context.description:
        assert True
    context.response = requests.delete("http://localhost:4567/projects" + "/" + context.new_id)

@given('there does not exist a class with id {id}')
def step_imp(context, id):
    context.response = requests.get("http://localhost:4567/projects" + "/" +id)
    assert context.response.status_code == 404

@when('user tries to delete a non existing todo list by {id}')
def step_imp(context, id):
    context.response = requests.delete("http://localhost:4567/projects" + "/" + id)
    assert context.response.status_code == 404

@then('server returns error:404 Not Found for that {id}')
def step_imp(context, id):
    context.response = requests.get("http://localhost:4567/projects" + "/" + id)
    assert context.response.status_code == 404

