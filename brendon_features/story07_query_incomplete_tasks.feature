Feature: Query incomplete tasks

(User story) As a student, I query the incomplete tasks for a class I am taking, to help manage my time.
(Author) Brendon



Scenario Outline: (Normal flow) Query all incomplete tasks
    Given The class <project_id> exists
    And The class has an <doneStatus> task with title <title>
    When I view all <doneStatus> tasks
    Then The task with title <title> will be present and be marked <doneStatus>

    Examples: Incomplete Tasks
        | project_id | title | doneStatus |
        | 1          | task1 | false      |
        | 1          | task2 | false      |
        | 1          | task3 | false      |


# Scenario Outline: (Alternate flow) Query all complete tasks
    Given The class <project_id> exists
    And The class has an <doneStatus> task with title <title>
    When I view all <doneStatus> tasks
    Then The task with title <title> will be present and be marked <doneStatus>

    Examples: Incomplete Tasks
        | project_id | title | doneStatus |
        | 1          | task1 | true       |
        | 1          | task2 | true       |
        | 1          | task3 | true       |


# Scenario Outline: (Error flow) Query all incomplete tasks
#     Given The class <project_id> exists
#     And The class has an incomplete task with title <title>
#     When I view all incomplete tasks
#     Then The task with title <title> should exist and be marked incomplete
# 
#     Examples: Incomplete Tasks
#         | project_id | title |
#         | 1          | task1 |
#         | 1          | task2 |
#         | 1          | task3 |
# 
# 
