from os import system
from behave import fixture, use_fixture
import requests
import socket
import json
from collections import defaultdict



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
        print('NOTE: quitting since server is NOT ACTIVE on 127.0.0.1 port: 4567')
        raise ThingifierServiceInactive



def after_all(context):
    print('after all !!')
    print(context.created_ids)

def before_all(context):
    # start the server
    verify_service_is_running()
    context.url = "http://localhost:4567/"
    print('before all')
    context.created_ids = defaultdict(list)
    # pass

def after_scenario(context, scenario):
    print(f'after scenario: {scenario}')
    print()
    print()
    # don't iterate over this since I need to delete values in created_ids dict
    the_created_ids = context.created_ids.copy()
    for endpoint, IDs in the_created_ids.items():
        base_url = context.url + '/' + endpoint + '/'
        print(f'endpoint: {endpoint}, IDs I am about to delete: {IDs}')
        while len(context.created_ids[endpoint]):
            for idx, ID in enumerate(IDs):
                print(f'    loop index: {idx}, ID: {ID}')
                resource = base_url + ID
                response = requests.delete(resource)
                if response.status_code == 200:
                    print(f'       response to delete: {response}')
                    context.created_ids[endpoint].remove(ID)
                    print(f'       no err after removing id: {ID}')
                else:
                    print(f'        HTTP Error code from delete request: {response.status_code}, resource: {resource}')
            print(f'finished iterating over: {IDs}, leftover IDs (should be all gone): {context.created_ids[endpoint]}')
            print()

    print(f'created_ids after a delete post scenario: {context.created_ids}')
    print()
    print()
