# Feature: Query high priority tasks
# 
# (User story) As a student,I query all incomplete HIGH priority tasks from all my classes,to identity my short-termgoals.
# (Author) Brendon
# 
# 
# 
# Scenario Outline: (Normal flow) Query all incomplete HIGH priority tasks
#     # already have
#     Given Three priority levels already exist in my system
#     And I am currently enrolled in two classes
#     And Both classes have a task with title <title> and priority <priority>
#     When I view all <doneStatus> <priority> priority tasks
#     Then The <priority> priority task with title <title> will be present and be marked <doneStatus>
# 
#     Examples: Incomplete High priority tasks
#         | title | doneStatus | priority |
#         | task1 | false      | HIGH     |
#         | task2 | false      | HIGH     |
#         | task3 | false      | HIGH     |
# 

# Scenario Outline: (Alternate flow) Query all complete HIGH priority tasks
#     # already have
#     Given Three priority levels already exist in my system
#     And I am currently enrolled in two classes
#     And Both classes have a task with title <title> and priority <priority>
#     When I view all <doneStatus> <priority> priority tasks
#     Then The <priority> priority task with title <title> will be present and be marked <doneStatus>
# 
#     Examples: Complete High priority tasks
#         | title | doneStatus | priority |
#         | task1 | true       | HIGH     |
#         | task2 | true       | HIGH     |
#         | task3 | true       | HIGH     |




# Scenario Outline: (Alternate flow) Query all complete tasks
#     Given The class <project_id> exists
#     And The class has an <doneStatus> task with title <title>
#     When I view all <doneStatus> tasks
#     Then The task with title <title> will be present and be marked <doneStatus>
# 
#     Examples: Incomplete Tasks
#         | project_id | title | doneStatus |
#         | 1          | task1 | true       |
#         | 1          | task2 | true       |
#         | 1          | task3 | true       |
# 
# 
# Scenario Outline: (Error flow) Query specific non-existant task
#     Given The class <project_id> exists
#     When I view all <doneStatus> tasks
#     Then The task with title <title> will be not present
# 
#     Examples: Incomplete Tasks
#         | project_id | title | doneStatus |
#         | 1          | task1 | true       |
#         | 1          | task2 | false      |
#         | 1          | task3 | true       |
# 
# 
