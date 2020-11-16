from os import system
from behave import fixture, use_fixture
import requests
import socket
import json
from collections import defaultdict
import logging
import os



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



def before_all(context):
    # start the server
    verify_service_is_running()
    context.base_url = "http://localhost:4567/"
    # print('before all')
    context.created_ids = defaultdict(list)
    # pass

def before_feature(context, feature):
    if feature.filename == 'story09_change_task_priority.feature':
        # print('before correct feature!!!')
        logging.basicConfig(
                filename='story9.log',
                filemode='w',
                level=logging.INFO,
                format='%(name)s - %(levelname)s - %(message)s',
        )


def after_scenario(context, scenario):
    if scenario.filename == 'story09_change_task_priority.feature':
        logging.info(f'after scenario: {scenario}')
        # don't iterate over this since I need to delete values in created_ids dict
        the_created_ids = context.created_ids.copy()
        for endpoint, IDs in the_created_ids.items():
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
        logging.info('')
        logging.info('')
