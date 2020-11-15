
from behave import *
import requests


"""
Step Definitions for story05_create_todo_list
"""

@when('user does a post request to the server with {title}')
def step_imp(context, title):
    context.response = requests.post("http://localhost:4567/projects", json={"title": title})
    context.response.json() == 201



@then('class with the name {title} is created')
def step_imp(context, title):
    classList = requests.get("http://localhost:4567/projects")



@when('user does a post request with {title} and  and {description}')
def step_imp(context,title,description):
    classname = {"title": title, "description":description}
    context.response_class2 = requests.post("http://localhost:4567/projects", json=classname )
    context.response_class2.json() == 201

@then('class with {title} and {description} is created')
def step_imp(context,title,description):
    context.className = {"title": title, "description":description}
    context.response = requests.get("http://localhost:4567/projects", json=context.className)
    context.response.json() == 200


@when('user does a bad post request to the server with {title} and {id}')
def step_imp(context,title,id):
    context.className = {"title":title, "id":id}
    context.response_class = requests.post("http://localhost:4567/projects", json=context.className )
    context.response_class.json() == 400

@then('"Error 400 Bad Request" will happen for that {title} and {id}')
def step_imp(context,title,id):
    context.className = {"title": title, "id": id}
    context.response_class = requests.get("http://localhost:4567/projects", json=context.className)
    context.response_class.json() == 400


