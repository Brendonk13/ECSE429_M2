Feature: Change task description

(User story) As a student, I want to change a task description, to better represent the work to do.
​(Author) Helen Lin
(todo) is there such thing as invalid description

  Scenario Outline: (Normal flow) Update a valid task with a new description
    Given I have an existing valid task with title <title> and description <oldDescription>
      And the new description <newDescription> is not the same as the old description <oldDescription>
     When I update the description to <newDescription>
     Then the task with title <title> should have description <newDescription>
      And the task with title <title> should not have description <oldDescription>
      
    Examples: 
      | title      | oldDescription    | newDescription            |
      | task1      | valid description | more detailed description |
      | homework   | do homework       | do textbook practice      |
      | assignment | do assignment     | create gherkin scripts    |

  Scenario Outline: (Alternate flow) Add a description to a valid task with no description
    Given I have an existing valid task with title <title> and no description
     When I update the description to <description>
     Then the task with title <title> should have description <description>
      
    Examples: 
      | title      | description   |
      | task1      | description   |
      | homework   | do homework   |
      | assignment | do assignment |

  Scenario Outline: (Alternate flow) Update a valid task with the same description
    Given I have an existing valid task with title <title> and description <oldDescription>
      And the new description <newDescription> is the same as the old description <oldDescription>
     When I update the description to <newDescription>
     Then the task with title <title> should have description <newDescription>
      
    Examples: 
      | title      | oldDescription    | newDescription            |
      | task1      | valid description | valid description         |
      | homework   | do homework       | do homework               |
      | assignment | do assignment     | do assignment             |

  Scenario Outline: (Error flow) Update a valid task with an invalid new description
    Given I have an existing valid task with title <title> and description <oldDescription>
      And the new description <newDescription> is not the same as the old description <oldDescription>
     When I update the description to <newDescription>
     Then the task with title <title> should have description <oldDscription>
      And the task with title <title> should not have description <newDescription>
      
    Examples: 
      | title      | oldDescription    | newDescription            |
      | task1      | valid description | toolong-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa |
      | homework   | do homework       | ""      |