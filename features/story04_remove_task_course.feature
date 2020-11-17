# Created by Helen Lin
Feature: Remove a task from a course
As a student, I remove an unnecessary task from my course to do list,so I can forget about it.

  Scenario Outline: (Normal flow) Remove an existing task from course
    Given I have an existing course <course>
      And I have an existing valid task with title <title>
      And this task is already added to the course
     When I remove the task from this course
     Then the course should not have the task anymore
  
    Examples: 
      | course  | title        |
      | ECSE362 | Assignment9  | 
      | ECSE415 | Assignment4  | 
      | ECSE429 | ProjectPartB | 

  Scenario Outline: (Alternate flow) Mark task as done and remove from course
    Given I have an existing course <course>
      And I have an existing valid task with title <title>
      And this task is already added to the course
     When I mark the task as done
      And I remove the task from this course
     Then the course should not have the task anymore
  
    Examples: 
      | course  | title        |
      | COMP251 | study        | 
      | FACC400 | blogpost     | 
      | ECSE458 | report       | 

  Scenario Outline: (Error flow) Remove task from invalid course
    Given I do not have existing course <course>
      And I have an existing valid task with title <title>
     When I remove the task from this course
     Then there should be an error returned from the system
  
    Examples: 
      | course  | title        |
      | invalid | homework     | 
      | test    | project      | 


