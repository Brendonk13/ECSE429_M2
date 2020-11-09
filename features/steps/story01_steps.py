from behave import *

## ------------STORY/FEATURE 1: Categorize tasks by priority ----------------------------------------
#scenario 1 - valid new task with priority
@given(u'I have three precreated priority levels in my system')
def step_impl(context):
    #client = Client("http://127.0.0.1:8000/soap/")
    #context.response = client.Allocate(customer_first='Firstname',
    #    customer_last='Lastname', colour='red')

#@then('I should receive an OK SOAP response')
#def step_impl(context):
  # eq_(context.response['ok'], 1)Given 
     
@when(u'I create a new task with title {title} and priority level {priority}')
def step_impl(context, title, priority):
    #store task id in context.taskID

@then(u'the task should have category {priority}')
def step_impl(context, priority):

#scenario 2 - valid existing task with priority
@given(u'I have an existing valid task with title {title}')
def step_impl(context, title):
    # create task with title
    #store id in context.taskID
    
@when(u'I add the task to the category {priority}')
def step_impl(context, priority):


# scenario 3 - invalid task
@given(u'I do not have an existing valid task with id {invalidID}')
def step_impl(context, invalidID):

@then(u'Then there should be an error returned from the system')
def step_impl(context):
    # check context.response for error code

@then(u'there should be no task with id {invalidID}')
def step_impl(context, invalidID):
   
# scenario 4 - invalid priority
@given(u'{priority} is not the name of an existing category')
def step_impl(context, priority):

@then(u'the task should not have category {priority})
def step_impl(context, priority):