from behave import *
# NOTE: conversion from feature ie: "Given I have three precreated priority levels in my system" IS A MACRO REGISTER W



# ===================== normal flow ============================================
@given('I have three precreated priority levels in my system')
def step_impl(context):
    pass

@given('And I have an existing valid task with title <title> and priority <oldPriority>')
def step_impl(context):
    pass

@given('And the new priority <newPriority> is not the same as the old priority <oldPriority>')
def step_impl(context):
    pass

@when('the category <newPriority>')
def step_impl(context):
    pass

@then('Then the task should have category <newPriority>')
def step_impl(context):
    pass

@then('And the task should not have category <oldPriority>')
def step_impl(context):
    pass
# ===================== normal flow ============================================



# ===================== alternate flow =========================================
@given('Given I have three precreated priority levels in my system')
def step_impl(context):
    pass

# @given('And I have an existing valid task with title <title> and priority <oldPriority>')
# def step_impl(context):
#     pass

@given('And the new priority <newPriority> is the same as the old priority <oldPriority>')
def step_impl(context):
    pass

@when('When I add the task to the category <newPriority>')
def step_impl(context):
    pass

# @then('Then the task should have category <newPriority>')
# def step_impl(context):
#     pass

# ===================== alternate flow =========================================
