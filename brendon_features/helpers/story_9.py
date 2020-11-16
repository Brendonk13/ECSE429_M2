import json
import requests
import logging


class Task:
    def __init__(self, title, priority, ID, response, description, url):
        self.title = title
        # self.description = description
        self.priority = priority
        self.created_id = ID
        self.response = response
        self.description = description
        self.url = url

    def __add__(self, other):
        # need cuz used in "after_scenario" for this feature
        return self.created_id + other

    def __radd__(self, other):
        return other + self.created_id

    def __repr__(self):
        return self.created_id


# default None for setup_environment fxn
# it doesn't actually create a task but does everything else
def create_task(context, title, description, priority):
    # create a task object storing basic response information
    # and return the ID of the object just created
    params = {"title": title, "description": description}
    body = {'data': json.dumps(params)}
    response = requests.post(context.url, **body)
    response_body = response.json()
    logging.info(f'response to post {context.endpoint}: {response_body}')
    assert response.ok

    ID = response_body["id"]
    if all((context.endpoint.startswith('categories/'),
            context.endpoint.endswith('/todos'))):
        response = requests.get(context.base_url + 'categories').json()
        category_id = category_id_from_priority(context, priority)
        new_ID = get_todo_id(response, category_id)
        new_ID = str(max(int(new_ID), int(ID)))
        logging.info(f'old ID: {ID},  new ID: {new_ID}')
        ID = new_ID
    task = Task(title, priority, ID, response_body, description, context.url)
    # context.prev_task = task
    return task


def setup_context_url_stuff(context, endpoint):
    context.endpoint = endpoint
    context.url = context.base_url + endpoint


def get_todo_id(response, obj_ID):
    for category in response['categories']:
        if obj_ID == category['id']:
            return category['todos'][-1]['id']


def get_todo_id(response, obj_ID):
    for category in response['categories']:
        if obj_ID == category['id']:
            return category['todos'][-1]['id']



def category_id_from_priority(context, priority):
    for category in context.init_env:
        if category.priority == priority:
            return category.created_id


