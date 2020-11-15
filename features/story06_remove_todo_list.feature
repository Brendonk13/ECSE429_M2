# Created by odaci at 2020-11-15
Feature: Remove a todo list for a class
  As a student, I want to remove a todo list for a class
  which i am no longer taking
  so that i can declutter my schedule
  # Enter feature description here

  Scenario Outline: Delete a todo list for a class (Normal Flow)
    Given there exists a class with name <title>
    When user does a delete request to the server
    Then class with name <title> is removed
    Examples:
      | title     |
      | Comp350   |
      | Ecse428   |

  Scenario Outline: Set a class as completed instead of deleting (Alternate Flow)
    Given there exists a class with name <title>
    And <isCompleted> as false
    When user does a post request with <new_isCompleted> as true
    Then class with name <title>
    Examples:
      | title     | isCompleted | new_isCompleted   |
      | Comp350   | false       | true              |
      | Ecse428   | false       | true              |
  Scenario Outline: Delete a class that doesn't exists (Error Flow)
    Given there doesn't exist a class with name <title>
    When user does a delete request to the server
    Then server returns "error:404 Not Found"
    Examples:
      | title           |
      | no_Class_exist  |
      | class_not_found | 


