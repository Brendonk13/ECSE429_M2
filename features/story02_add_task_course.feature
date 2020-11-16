# Created by Helen Lin
Feature: Add a task to a course
As a student, I add a task to a course to do list, so I can remember it.

  Scenario Outline: (Normal flow) Add an existing task to a course's to-do list
    Given I have an existing course <course>
      And I have an existing valid task with title <title>
     When I add the task to the course
     Then the task should be a task of <course>
      And the course should have the task with title <title> in its list
  
    Examples: 
      | course  | title        |
      | ECSE362 | Assignment9  | 
      | ECSE415 | Assignment4  | 
      | ECSE429 | ProjectPartB | 

  Scenario Outline: (Alternate flow) Add a new task to a course's to-do list
    Given I have an existing course <course>
     When I create a new task with title <title>
      And I add the task to the course
     Then the task should be a task of <course>
      And the course should have the task with title <title> in its list
      
    Examples: 
      | course  | title        |
      | COMP251 | study        | 
      | FACC400 | blogpost     | 
      | ECSE458 | report       | 

  Scenario Outline: (Error flow) Add a task to an invalid course
    Given I do not have existing course <course>
      And I have an existing valid task with title <title>
     When I add the task to the course
     Then there should be an error returned from the system
  
    Examples: 
      | course  | title        |
      | invalid | homework     | 
      | test    | project      | 

   Scenario Outline: (Error flow) Add an invalid task to a valid course
    Given I have an existing course <course>
      And there is no task in the system with id <id>
     When I add the task to the course
     Then there should be an error returned from the system
  
    Examples: 
      | course  | id        |
      | invalid | 11111     | 
      | test    | 22222     | 

