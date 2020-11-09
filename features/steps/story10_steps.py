from behave import *

## ------------STORY/FEATURE 10: Update task description ----------------------------------------
## helen lin
#scenario 1 - valid update description
@given(u'I have an existing valid task with title {title} and description {oldDescription}')
def step_impl(context, title, oldDescription):
    # store id of task in context.taskID
     
@given(u'the new description {newDscription} is not the same as the old description {oldDescription}')
def step_impl(context, newDescription, oldDescription):

@when(u'I update the description to {description}')
def step_impl(context, description):

@then(u'the task should have description {description}')
def step_impl(context, description):

@then(u'the task should not have description {oldDescription}')
def step_impl(context, oldDescription):

#scenario 2 - valid existing task with no previous description
@given(u'I have an existing valid task with title {title} and no description')
def step_impl(context, title):
    # store id of task in context.taskID
    
#scenario 3 - update valid task with same description
@given(u'the new description {newDscription} is the same as the old description {oldDescription}')
def step_impl(context, newDescription, oldDescription):

# scenario 4 - invalid description
# already implemented