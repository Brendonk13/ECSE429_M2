Feature: Query incomplete tasks

(User story) As a student, I query the incomplete tasks for a class I am taking, to help manage my time.
(Author) Brendon



Scenario Outline: (Normal flow) Query all incomplete tasks
    Given The class <class_id> exists
    And The class has an incomplete task with title <title>
    When I view all incomplete tasks
    Then The incomplete task with title <title> should exist and be marked incomplete

    Examples: Incomplete Tasks
        | class_id | title |
        | 1        | task1 |
        | 1        | task2 |
        | 1        | task3 |


# Scenario Outline: (Alternate flow) Query all incomplete tasks
#     Given There exists an incomplete task with title <title>
#         When I view all incomplete tasks
#         Then The incomplete task with title <title> should exist and be marked incomplete
# 
#     Examples: Incomplete Tasks
#         | title |
#         | task1 |
#         | task2 |
#         | task3 |


