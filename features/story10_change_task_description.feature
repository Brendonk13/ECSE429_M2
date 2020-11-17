# Created by Helen Lin
Feature: Change task description
As a student, I want to change a task description, to better represent the work to do.

  Scenario Outline: (Normal flow) Update a valid task with a new description
    Given I have an existing valid task with title <title> and description <oldDescription>
      And the new description <newDescription> is not the same as the old description <oldDescription>
     When I update the description to <newDescription>
     Then the task should have description <newDescription>
      
    Examples: 
      | title      | oldDescription    | newDescription            |
      | task1      | valid description | more detailed description |
      | homework   | do homework       | do textbook practice      |
      | assignment | do assignment     | create gherkin scripts    |

  Scenario Outline: (Alternate flow) Add a description to a valid task with no description
    Given I have a valid task with title <title> and no description
     When I update the description to <description>
     Then the task should have description <description>
      
    Examples: 
      | title      | description   |
      | task1      | description   |
      | homework   | do homework   |
      | assignment | do assignment |

  Scenario Outline: (Alternate flow) Update a valid task with the same description
    Given I have an existing valid task with title <title> and description <oldDescription>
      And the new description <newDescription> is the same as the old description <oldDescription>
     When I update the description to <newDescription>
     Then the task should have description <oldDescription>
    
    Examples: 
      | title      | oldDescription    | newDescription            |
      | task1      | valid description | valid description         |
      | homework   | do homework       | do homework               |
      | assignment | do assignment     | do assignment             |

  Scenario Outline: (Error flow) Update a task that doesn't exist with a description
    Given there is no task in the system with id <id>
     When I update the description to <description>
     Then there should be an error returned from the system
      
    Examples: 
      | id      | description       | 
      | 1111    | valid description | 
      | 2222    | do homework       | 
