from os import system
from behave import fixture, use_fixture
from requests import post
import socket
import json



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


@fixture
def create_priorities(context, priorities=None):
    url = context.url + "projects/1/tasks"
    for idx, priority in enumerate(priorities):
        title = "project task: {}".format(idx)
        description = "Priority: {} a good description".format(priority)
        params = {"title": title, "description": description}

        body = {'data': json.dumps(params)}
        response = post(url, **body).json()
        print('response to post projects/1/tasks: {}'.format(response))




def before_all(context):
    # start the server
    verify_service_is_running()
    context.url = "http://localhost:4567/"
    print('before all')
    # pass


def before_tag(context, tag):
    if tag == "fixture.create_priorities_HML":
        # HML for High, Medium, Low
        priorities = [ 'HIGH', 'MEDIUM', 'LOW' ]
        use_fixture(create_priorities, context, priorities)
