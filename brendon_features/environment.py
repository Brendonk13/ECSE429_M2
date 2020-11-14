from os import system

def before_all(context):
    # start the server
    result = system('java -jar ../runTodoManagerRestAPI-1.5.5.jar')
    print('before_all: java -jar result: {}'.format(result))
    # pass
