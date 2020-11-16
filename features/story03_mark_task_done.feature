# Created by Helen Lin
Feature: Mark a task as done
As a student, I mark a task as done on my course to do list, so I can track my accomplishments.

  Scenario Outline: (Normal flow) Mark an existing task as done
    Given I have an existing valid task with title <title>
     When I mark the task as done
     Then the task should be marked as done
  
    Examples: 
      | title        |
      | Assignment9  | 
      | Assignment4  | 
      | ProjectPartB | 

  Scenario Outline: (Alternate flow) Mark a new task as done
     When I create a new task with title <title>
      And I mark the task as done
     Then the task should be marked as done
      
    Examples: 
      | title        |
      | study        | 
      | blogpost     | 
      | report       | 

  Scenario Outline: (Error flow) Mark an invalid task as done
    Given there is no task in the system with id <id>
     When I mark the task as done
     Then there should be an error returned from the system
  
    Examples: 
      | id        |
      | 11111     | 
      | 22222     | 

