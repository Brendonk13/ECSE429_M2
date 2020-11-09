Feature: Create Pick List

As a Lego(R) Part Warehouse Operator
I would like to create a pick list from a customer order
So that a warehouse picker will be able to fulfill the specific order for the customer

Scenario: Pick Several Valid Products (Normal Flow)

Given user Fizbin is logged on as the operator
And the inventory has been initialized
When the following products are requested
      |Quantity  |Part     |
      |100       |3001old  |
      |20        |645a     |
      |2         |bb19     |
Then the following pick list is returned
      |Bin      |Quantity  |Part     |
      |bin1900  |100       |3001old  |
      |bin2011  |20        |645a     |
      |bin1892  |2         |bb19     |



	  
Scenario: Pick One Valid Product (Alternate Flow)

Given user Fizbin is logged on as the operator
And the inventory has been initialized
When the quantity 25 of Part 645 is requested
Then the following pick list is returned
      |Bin      |Quantity  |Part  |
      |bin2010  |25        |645   |     

Scenario: Pick Several Valid Products Including Duplicates (Alternate Flow)
Given user Fizbin is logged on as the operator
And the inventory has been initialized
When the following products are requested
      |Quantity  |Part     |
      |100       |3001old  |
      |20        |645a     |
      |123       |3001old  |
      |2         |bb19     |     
Then the following pick list is returned
      |Bin      |Quantity  |Part     |
      |bin1900  |223       |3001old  |
      |bin2011  |20        |645a     |
      |bin1892  |2         |bb19     |
	  

Scenario: Pick List of Several Products including 1 Invalid Product (Error Flow)

Given user Fizbin is logged on as the operator
And the inventory has been initialized
When the following products are requested
      |Quantity  |Part     |
      |100       |3001old  |
      |20        |happyface|
      |2         |bb19     |  
Then the following pick list is returned
      |Bin      |Quantity  |Part     |
      |bin1900  |100       |3001old  |
      |Part DNE |20        |happyface|
      |bin1892  |2         |bb19     |

	  
	  
	  
	  
	  
	  
	  
	  
Scenario: Pick List of Several Products including 2 Invalid Products (Error Flow)

Given user Fizbin is logged on as the operator
And the inventory has been initialized
When the following products are requested
      |Quantity  |Part     |
      |100       |3001old  |
      |20        |happyface|
      |2         |lemonpie |    
Then the following pick list is returned
      |Bin      |Quantity  |Part     |
      |bin1900  |100       |3001old  |
      |Part DNE |20        |happyface|
      |Part DNE |2         |lemonpie |


	  
	  
	  
	  
	  
	  
	  
	  
Scenario: Pick List of Several Products including all Invalid Products (Error Flow)

Given user Fizbin is logged on as the operator
And the inventory has been initialized
When the following products are requested
      |Quantity  |Part     |
      |100       |sadface  |
      |20        |happyface|
      |2         |lemonpie |
Then the following pick list is returned
      |Bin      |Quantity  |Part     |
      |Part DNE |100       |3001old  |
      |Part DNE |20        |happyface|
      |Part DNE |2         |bb19     |


	  
	  
	  
	  
	  
	  
	  
	  
Scenario: Invalid Operator Attempts to Pick One Valid Product (Error Flow)

Given user Undefined is logged on as the operator
And the inventory has been initialized
When the quantity 25 of Part 645 is requested
Then the error message "User Undefined System Cannot Generate Picklist" is returned

Scenario: Suspended Operator Attempts to Pick One Valid Product (Error Flow)

Given user Suspended is logged on as the operator
And the inventory has been initialized
When the quantity 25 of Part 645 is requested
Then the error message "User Suspended System Cannot Generate Picklist" is returned











Scenario: Single Product Request Fulfilled from Multiple Bins (Alternate Flow)

Given user Fizbin is logged on as the operator
And the inventory count is defined to be
      |Bin      |Part     |Count  |
      |bin3000  |3001old  |200    |
      |bin3001  |3001old  |200    |
      |bin3002  |645a     |400    |
      |bin3003  |645a     |50     |
      |bin3004  |bb19     |125    |
      |bin3005  |bb19     |75     |    
When the quanity 225 of product 3001old is requested
The the following pick list is returned
      |Bin      |Quantity  |Part     |
      |bin3000  |200       |3001old  |
      |bin3001  |25        |3001old  |


	  
	  
	  
	  
	  
	  
Scenario: Single Product Request Insufficient Quantity from Bins (Error Flow)

Given user Fizbin is logged on as the operator
And the inventory count is defined to be
      |Bin      |Part     |Count  |
      |bin3000  |3001old  |200    |
      |bin3002  |645a     |400    |
      |bin3004  |bb19     |125    |    
When the quantity 225 of product 3001old is requested
The the following pick list is returned
      |Bin      |Quantity  |Part     |
      |bin3000  |200       |3001old  |
      |SHORTFALL|25        |3001old  |
      

	  
	  
	  
	  
	  
	  
	  
	  
	  
Scenario: Multiple Product Request Fullfilled from Multiple Bins (Alternate Flow)

Given user Fizbin is logged on as the operator
And the inventory count is defined to be
      |Bin      |Part     |Count  |
      |bin3000  |3001old  |200    |
      |bin3001  |3001old  |200    |
      |bin3002  |645a     |400    |
      |bin3003  |645a     |50     |
      |bin3004  |bb19     |125    |
      |bin3005  |bb19     |75         
When the following products are requested
      |Quantity  |Part   |
      |225       |3001old|
      |150       |bb19   |
      |200       |645a   |
Then the following pick list is returned
      |Bin      |Quantity  |Part     |
      |bin3000  |200       |3001old  |
      |bin3001  |25        |3001old  |
      |bin3004  |125       |bb19     |
      |bin3005  |25        |bb19     |
      |bin3002  |200       |645a     |
     
Scenario: Multiple Product Request Insufficient Quantity from Multiple Bins (Error Flow)

Given user Fizbin is logged on as the operator
And the inventory count is defined to be
      |Bin      |Part     |Count  |
      |bin3000  |3001old  |200    |
      |bin3001  |3001old  |200    |
      |bin3002  |645a     |400    |
      |bin3003  |645a     |50     |
      |bin3004  |bb19     |125    |
When the following products are requested
      |Quantity  |Part   |
      |425       |3001old|
      |250       |bb19   |
      |200       |645a   |
Then the following pick list is returned
      |Bin      |Quantity  |Part     |
      |bin3000  |200       |3001old  |
      |bin3001  |200       |3001old  |
      |SHORTFALL|25        |3001old  |
      |bin3004  |125       |bb19     |
      |SHORTFALL|125       |bb19     |
      |bin3002  |200       |645a     |
      
