# Created by Helen Lin
Feature: Categorize tasks by priority
As a student, I categorize tasks as HIGH, MEDIUM or LOW priority, so I can better manage my time.

  Scenario Outline: (Normal flow) Create a new valid task with a given priority
    Given I have three precreated priority levels in my system
     When I create a new task with title <title> and priority level <priority>
     Then the task should have category <priority>
  
    Examples: 
      | title      | priority |
      | new_task_1 | HIGH     | 
      | new_task_2 | MEDIUM   | 
      | new_task_3 | LOW      | 

  Scenario Outline: (Alternate flow) Categorize an existing valid task by a given priority
    Given I have three precreated priority levels in my system
      And I have an existing valid task with title <title>
     When I add the task to the category <priority>
     Then the task should have category <priority>
      
    Examples: 
      | title | priority |
      | task1 | HIGH     | 
      | task2 | MEDIUM   | 
      | task3 | LOW      | 

  Scenario Outline: (Error flow) Categorize a valid task by an invalid priority
    Given I have three precreated priority levels in my system
      And <priority> is not the name of an existing category
      And I have an existing valid task with title <title>
     When I add the task to the category <priority>
     Then the task should not have category <priority>
      And there should be an error returned from the system
      
    Examples: 
      | title | priority        |
      | task1 | med             | 
      | task2 | test            | 
      | task3 | invalid         |
