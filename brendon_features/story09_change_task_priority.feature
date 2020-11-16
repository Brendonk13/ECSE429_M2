@fixture.create_priorities_HML
Feature: Change task priority

(User story) As a student, I want to adjust the priority of a task, to help better manage my time.
(Author) Brendon


# Scenario Outline: (Normal flow) Update a valid task with a new priority
#     Given Three priority levels already exist in my system
#         And There exists a task with title <title> and priority <oldPriority>
#         And The new priority <newPriority> is different from the old priority <oldPriority>
#         When I add the relevant task to the category <newPriority>
#         Then The task should now have category <newPriority>
# 
#     Examples: Tasks
#         | title | oldPriority | newPriority |
#         | task1 | HIGH        | MEDIUM      |
#         | task2 | MEDIUM      | HIGH        |
#         | task3 | LOW         | HIGH        |
# 
# 
# Scenario Outline: (Alternate flow) Update a valid task with the same priority
#     Given Three priority levels already exist in my system
#         And There exists a task with title <title> and priority <oldPriority>
#         And The new priority <newPriority> is the same as the old priority <oldPriority>
#         When I add the relevant task to the category <newPriority>
#         Then The task should now have category <newPriority>
# 
#     Examples:
#         | title | oldPriority | newPriority |
#         | task1 | HIGH        | HIGH        |
#         | task2 | MEDIUM      | MEDIUM      |
#         | task3 | LOW         | LOW         |
# 
# 
# 
# Scenario Outline: (Error flow) Update a valid task with non-existant priority
#     # NOTE: test that this actually registers as an error first !
#     Given Three priority levels already exist in my system
#         And There exists a task with title <title> and priority <oldPriority>
#         And the new priority for this task: <newPriority> does not exist
#         When I add the task to the non-existant category <newPriority>
#         Then task should not be added to the category <newPriority>
# 
#     Examples:
#         | title | oldPriority | newPriority |
#         | task1 | HIGH        | nope_1      |
#         | task2 | MEDIUM      | nope_2      |
#         | task3 | LOW         | nope_3      |
