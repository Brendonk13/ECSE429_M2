#Feature: Look up a postage rate for sending an item
#In order to determine whether and how to send an item
#As an item sender
#I want to find out the postage rates when I enter the dimensions, weight and destination
#
#​
#
#  Scenario Outline: Send an item domestically in Canada or the US
#    Given I am sending an item from <sourceCountry>
#      And I am sending the item domestically from <sourceState> to <targetState>
#      And the length of the item is <lengthNum> <lengthUnit>
#      And the width of the item is <widthNum> <widthUnit>
#      And the height of the item is <heightNum> <heightUnit>
#      And the weight of the item is <weightNum> <weightUnit>
#     When I click "Get Rate"
#     Then the result should be <price> for <postType> post
#  
#    Examples: 
#      | sourceCountry | sourceState               | targetState               | lengthNum | lengthUnit | widthNum | widthUnit | heightNum | heightUnit | weightNum | weightUnit | price  | postType                       | 
#      | Canada        | Alberta                   | Nunavut                   | 18        | cm         | 9        | cm        | 0.5       | cm         | 2         | g          | $0.57  | Postcard                       | 
#      | Canada        | Nova Scotia               | Ontario                   | 24        | cm         | 13.2     | cm        | 0.25      | cm         | 22        | g          | $0.57  | Standard Letter (Regular)      | 
#      | Canada        | Quebec                    | Yukon                     | 23.5      | cm         | 10       | cm        | 0.4       | cm         | 30        | g          | $1.10  | Medium Letter (Regular)        | 
#      | Canada        | Newfoundland and Labrador | Manitoba                  | 20.2      | cm         | 15.1     | cm        | 0.2       | cm         | 41        | g          | $1.22  | Non-standard Letter (Regular)  | 
#      | Canada        | Northwest Territories     | Prince Edward Island      | 15        | cm         | 15       | cm        | 0.15      | cm         | 30        | g          | $0.67  | Standard Letter (Priority)     | 
#      | Canada        | British Columbia          | New Brunswick             | 23        | cm         | 16.3     | cm        | 0.48      | cm         | 49.98     | g          | $1.20  | Medium Letter (Priority)       | 
#      | Canada        | Saskatchewan              | Saskatchewan              | 38        | cm         | 27       | cm        | 2         | cm         | 100       | g          | $1.32  | Non-standard Letter (Priority) | 
#      | Canada        | Yukon                     | Nova Scotia               | 14        | cm         | 9        | cm        | 0.13      | cm         | 1         | g          | $0.77  | Standard Letter (Express)      | 
#      | Canada        | Prince Edward Island      | Quebec                    | 23.49     | cm         | 9.05     | cm        | 0.49      | cm         | 0.01      | g          | $1.30  | Medium Letter (Express)        | 
#      | Canada        | Manitoba                  | Ontario                   | 15        | cm         | 15       | cm        | 0.2       | cm         | 15        | g          | $1.42  | Non-standard Letter (Express)  | 
#      | Canada        | Nunavut                   | Yukon                     | 45        | cm         | 9        | cm        | 8         | cm         | 150       | g          | $6.42  | Domestic Regular Parcel        | 
#      | Canada        | Nova Scotia               | Northwest Territories     | 200       | cm         | 200      | cm        | 200       | cm         | 30000     | g          | $39.06 | Domestic Priority Parcel       | 
#      | Canada        | Ontario                   | Newfoundland and Labrador | 10        | cm         | 7        | cm        | 0.1       | cm         | 0.1       | g          | $7.16  | Domestic Express Parcel        | 
#      | Canada        | Alberta                   | Nunavut                   | 9         | cm         | 0.5      | cm        | 18        | cm         | 2         | g          | $0.57  | Postcard                       | 
#      | Canada        | New Brunswick             | British Columbia          | 50        | cm         | 50       | cm        | 50        | cm         | 10        | kg         | $12.28 | Domestic Regular Parcel        | 
#      | USA           | Delaware                  | Kansas                    | 15        | cm         | 9.25     | cm        | 0.04      | cm         | 3         | g          | $0.28  | US First-Class Postcard        | 
#      | USA           | New York                  | New York                  | 29.21     | cm         | 15.5575  | cm        | 0.635     | cm         | 99.22     | g          | $0.95  | US First-Class Letter          | 
#      | USA           | Texas                     | Maine                     | 29.21     | cm         | 15.5575  | cm        | 0.635     | cm         | 0.01      | g          | $0.88  | US First-Class Large Envelope  | 
#      | USA           | New Jersey                | California                | 35        | cm         | 90       | cm        | 90        | cm         | 320       | g          | $3.09  | US First-Class Package         | 
#  
#  ​
