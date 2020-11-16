@fixture.create_priorities_HML
Feature: Change task priority

(User story) As a student, I want to adjust the priority of a task, to help better manage my time.
(Author) Brendon


Scenario Outline: (Normal flow) Update a valid task with a new priority
    Given I have three precreated priority levels in my system
        And I have an existing valid task with title <title> and priority <oldPriority>
        And the new priority <newPriority> is not the same as the old priority <oldPriority>
        When I add the task to the category <newPriority>
        Then the task should have category <newPriority>

    Examples: Tasks
        | title | oldPriority | newPriority |
        | task1 | HIGH        | MEDIUM      |
        | task2 | MEDIUM      | HIGH        |
        | task3 | LOW         | HIGH        |


# Scenario Outline: (Alternate flow) Update a valid task with the same priority
#     Given I have three precreated priority levels in my system
#         And I have an existing valid task with title <title> and priority <oldPriority>
#         And the new priority <newPriority> is the same as the old priority <oldPriority>
#         When I add the task to the category <newPriority>
#         Then the task should have category <newPriority>
# 
#     Examples:
#         | title | oldPriority | newPriority |
#         | task1 | HIGH        | HIGH        |
#         | task2 | MEDIUM      | MEDIUM      |
#         | task3 | LOW         | LOW         |



# Scenario Outline: (Error flow) Update a valid task with negative priority
#     # NOTE: test that this actually registers as an error first !
#     Given I have three precreated priority levels in my system
#         And I have an existing valid task with title <title> and priority <oldPriority>
#         And the new priority <newPriority> is the same as the old priority <oldPriority>
#         When I add the task to the category <newPriority>
#         Then the task should have category <newPriority>
# 
#     Examples:
#         | title | oldPriority | newPriority |
#         | task1 | HIGH        | HIGH        |
#         | task2 | MEDIUM      | MEDIUM      |
#         | task3 | LOW         | LOW         |
