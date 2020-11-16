# Created by odaci at 2020-11-15
Feature: Remove a todo list for a class
  As a student, I want to remove a todo list for a class
  which i am no longer taking
  so that i can declutter my schedule
  # Enter feature description here

  Scenario Outline: Delete a todo list for a class (Normal Flow)
    Given there is a class with name <title>
    When user does a delete request to the server with <title>
    Then class with name <title> is removed
    Examples:
      | title     |
      | Comp350   |
      | Ecse428   |


  Scenario Outline: Set a class as completed instead of deleting (Alternate Flow)
    Given there exists a class with name <title> and <description> as false
    When user does a post request with <new_description> as true
    Then class with name <title> , <new_description> has a new description of NOT TAKING ANYMORE
    Examples:
      | title     | description                       | new_description                   |
      | Comp360   | Comp class taking this year       | NOT TAKING ANYMORE                |
      | Ecse458   | Ecse Class taking this year       | NOT TAKING ANYMORE                |
  Scenario Outline: Delete a class that doesn't exists (Error Flow)
    Given there does not exist a class with id <id>
    When user tries to delete a non existing todo list by <id>
    Then server returns error:404 Not Found for that <id>
    Examples:
      | id           |
      | 99999        |
      | 000000       |


