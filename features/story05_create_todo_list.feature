# Created by odaci at 2020-11-15
Feature: Create todo list for a new class
  As a student, I want to create a todo list for a new class I am taking
  so that I can manage course work.

  Scenario Outline: Create a todo list for a new class (Normal Flow)
    Given user provides <title> for a class name
    When user does a post request to the server
    Then class with the name <title> is created
    Examples:
      | title       |
      | new_class_1 |
      | new_class_2 |
      | new_class_3 |
  Scenario Outline: Create a todo list for a new class with completed and description (Alternate Flow)
    Given user provides <title> for a class name
    And provides <isCompleted> for the class progress
    And provides <description> for class details
    When user does a post request
    Then class with name, progress and details is created
    Examples:
      | title         | isCompleted | description                         |
      | new_class_1   | false       | I joined New class 1                |
      | new_class_2   | false       | I registered for New class 2        |
      | new_class_3   | true        | I joined New class 3                |

  Scenario Outline: Create a todo list for a new class by providing class id (Error Flow)
    Given user provides <title> for a class name
    And <id> for a class id
    When user does a post request
    Then "Error 400 Bad Request" will happen
    Examples:
      | title       | id        |
      | new_class_1 | 101       |
      | new_class_2 | 102       |



