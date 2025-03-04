from os import system
from behave import fixture, use_fixture
import requests
import socket
from collections import defaultdict
import logging
import os
from helpers.story_9 import Task, create_task, setup_context_url_stuff



class ThingifierServiceInactive(Exception):
    """
        Only ever raised if port_is_open() function returns false (in ImmutableRequest.__init__)
    """
    pass


def verify_service_is_running():
    def port_is_open():
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        location = ("127.0.0.1", 4567)
        return a_socket.connect_ex(location) == 0

    if not port_is_open():
        print('ERROR: quitting since server is NOT ACTIVE on 127.0.0.1 port: 4567')
        raise ThingifierServiceInactive


def setup_story9_environment(context, priorities):
    # create 3 priority levels by creating 3 tasks with different priorities
    context.init_env = []
    for priority in priorities:
        title = "Priority: {}".format(priority)
        description = "{} Priority Tasks".format(priority)

        task = create_task(context, title, description, priority)
        context.created_ids[context.endpoint].append(task)
        context.init_env.append(task)


def before_all(context):
    # start the server
    verify_service_is_running()
    context.base_url = "http://localhost:4567/"
    # print('before all')
    context.created_ids = defaultdict(list)


def log_file_name(feature_name):
    if feature_name == 'story09_change_task_priority.feature':
        return 'story9.log'
    if feature_name == 'story07_query_incomplete_tasks.feature':
        return 'story7.log'
    if feature_name == 'story08_query_high_priority_tasks.feature':
        return 'story8.log'


def before_feature(context, feature):
    log_file = log_file_name(feature.filename)
    logging.basicConfig(
            filename=log_file,
            filemode='w',
            level=logging.INFO,
            format='%(name)s - %(levelname)s - %(message)s',
    )

    if log_file in ('story9.log', 'story8.log'):
        setup_context_url_stuff(context, 'categories')
        priorities = [ 'HIGH', 'MEDIUM', 'LOW' ]
        setup_story9_environment(context, priorities)
        context.dont_delete_after_scenario = ['categories']
        logging.info('setup feature story for log_file: {} completed'.format(log_file))

    if log_file == 'story7.log':
        # need this for compatibility with cleanup_created_ids function
        context.dont_delete_after_scenario = []

    # if log_file == 'story8.log':



def after_feature(context, feature):
    if feature.filename == 'story09_change_task_priority.feature':
        the_created_ids = context.created_ids.copy()
        cleanup_created_ids(context, the_created_ids.items(), after_scenario = False)



def after_scenario(context, scenario):
    if scenario.filename in (
                'story09_change_task_priority.feature',
                'story07_query_incomplete_tasks.feature'):

        logging.info('after scenario: {}'.format(scenario))
        # don't iterate over this since I need to delete values in created_ids dict
        the_created_ids = context.created_ids.copy()
        # the_created_ids['categories'] = []
        cleanup_created_ids(context, the_created_ids.items())
        # don't delete categories until after this feature



def cleanup_created_ids(context, dict_items, after_scenario=True):
    for endpoint, IDs in dict_items:
        if after_scenario:
            if endpoint in context.dont_delete_after_scenario:
                continue

        base_url = context.base_url + endpoint + '/'
        logging.info(f'endpoint: {endpoint}, IDs I am about to delete: {IDs}')
        while len(context.created_ids[endpoint]):
            for idx, ID in enumerate(IDs):
                logging.info(f'    loop index: {idx}, ID: {ID}')
                resource = base_url + ID
                response = requests.delete(resource)
                if response.status_code == 200:
                    logging.info(f'       response to delete: {response}')
                    context.created_ids[endpoint].remove(ID)
                    logging.info(f'       list after delete: {context.created_ids[endpoint]}')
                else:
                    logging.info(f'        HTTP Error code from delete request: {response.status_code}, resource: {resource}')
            logging.info(f'finished iterating over: {IDs}, leftover IDs (should be all gone): {context.created_ids[endpoint]}')
            logging.info('')

    logging.info(f'created_ids after a delete post scenario: {context.created_ids}')
    logging.info('====================== done scenario ===========================')
    logging.info('')
    logging.info('')
    logging.info('')
