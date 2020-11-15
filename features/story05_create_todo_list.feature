# Created by odaci at 2020-11-15
Feature: Create todo list for a new class
  As a student, I want to create a todo list for a new class I am taking
  so that I can manage course work.

  Scenario Outline: Create a todo list for a new class (Normal Flow)
    When user does a post request to the server with <title>
    Then class with the name <title> is created
    Examples:
      | title       |
      | new_class_1 |
      | new_class_2 |
      | new_class_3 |
  Scenario Outline: Create a todo list for a new class with  description (Alternate Flow)
    When user does a post request with <title> and  and <description>
    Then class with name, progress and details is created
    Examples:
      | title                | description                           |
      | comp500              | I joined Comp500                      |
      | comp600              | I registered for comp600              |
      | comp800              | I joined comp800                      |

  Scenario Outline: Create a todo list for a new class by providing class id (Error Flow)
    When user does a bad post request to the server with <title> and <id>
    Then "Error 400 Bad Request" will happen for that <title> and <id>
    Examples:
      | title       | id        |
      | new_class_1 | 101       |
      | new_class_2 | 102       |



