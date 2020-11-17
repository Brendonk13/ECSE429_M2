import json
import requests
import logging

class CategoryDoesNotExist(Exception):
    pass

class CategoryWithPriority:
    def __init__(self, category_response):
        self.priority = 'Priority: ' + category_response['description']
        self.created_id = category_response['id']
        # logging.info(f'

    def __repr__(self):
        return 'CategoryWith obj: Priority: {}, created_id: {}'.format(self.priority, self.created_id)

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
        logging.info(f'tried to print obj with id: {self.created_id}')
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

    response_ID = response_body["id"]
    ID = get_created_id(context, priority, response_ID)
    logging.info(f'response ID: {response_ID},  new ID: {ID}')

    task = Task(title, priority, ID, response_body, description, context.url)
    # context.prev_task = task
    return task


def get_created_id(context, priority, response_ID):
    if all((context.endpoint.startswith('categories/'),
            context.endpoint.endswith('/todos'))):
        category_id = category_id_from_priority(context, priority)

        response = all_categories_response(context)
        new_ID = todo_id_from_response(response, category_id)
        new_ID = str(max(int(new_ID), int(response_ID)))
        logging.info(f'old ID: {response_ID},  new ID: {new_ID}')

        created_id = new_ID
        return created_id
    return response_ID


def setup_context_url_stuff(context, endpoint):
    context.endpoint = endpoint
    context.url = context.base_url + endpoint


def todo_id_from_response(response, obj_ID):
    logging.info(f'todo_id_from_response, response: {response}')
    for category in response:
        if obj_ID == category['id']:
            return category['todos'][-1]['id']


def all_categories_response(context):
    obj_name = 'categories'
    return requests.get(context.base_url + obj_name).json()[obj_name]


def categories_with_priorities(context):
    return [
        CategoryWithPriority(category)
        for category
        in all_categories_response(context)
    ]


def category_id_from_priority(context, priority, search_all_priorities=False):
    categories = context.init_env
    if search_all_priorities:
        categories = categories_with_priorities(context)
        logging.info(f'fxn: categories_with_priorities: using categories: {categories}')

    # logging.info(f'categories: {categories}')
    logging.info(f'searching for priority: {priority}')
    for category in categories:
        logging.info(f'category: {category}')
        if category.priority == priority:
            if category == None:
                logging.info('category with correct priority is NONE')
            logging.info(f'found priority attached to  object: {category}')
            return category.created_id

    raise CategoryDoesNotExist


def create_todo_with_priority(context, priority, title):
    description = '{} Priority Tasks'.format(priority)

    priority_category_id = category_id_from_priority(context, priority)
    endpoint = 'categories/{}/todos'.format(priority_category_id)
    setup_context_url_stuff(context, endpoint)

    task = create_task(context, title, description, priority)

    # add resources that need to be deleted to restore state
    # response = all_categories_response(context)
    # todo_id = todo_id_from_response(response, priority_category_id)
    # endpoint = 'categories/{}/todos'.format(priority_category_id)

    return task


def delete_todo_with_priority(context, priority, todo_id):
    '''
        to do this we need to delete 2 resources:
        categories/category_id/todos/todo_id
        todos/todo_id
    '''
    category_id = category_id_from_priority(context, priority)
    endpoint = 'categories/{}/todos/{}'.format(category_id, todo_id)

    setup_context_url_stuff(context, endpoint)
    logging.info(f'DELETE: {context.url}')
    response = requests.delete(context.url)
    logging.info(response)
    assert response.ok

    url = context.base_url + 'todos/{}'.format(todo_id)
    logging.info(f'DELETE: {url}')
    response = requests.delete(url)
    logging.info(response)
    assert response.ok
    logging.info('')




def get_done_status(doneStatus):
    return True if doneStatus == 'true' else False
