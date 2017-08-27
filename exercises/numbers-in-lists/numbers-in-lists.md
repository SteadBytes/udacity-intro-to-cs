# Numbers in Lists
Define a procedure that takes in a string of numbers from 1-9 and outputs a list with the following parameters:
* Every number in the string should be inserted into the list. 
* If a number x in the string is less than or equal to the preceding number y, the number x should be inserted into a sublist.
* Continue adding the following numbers to the sublist until reaching a number z that
is greater than the number y. Then add this number z to the normal list and continue.

## Example Input and Output
```
string = '543987'
print(numbers_in_lists(string))
>>> [5,[4,3],9,[8,7]]

string= '987654321'
print(numbers_in_string([9,[8,7,6,5,4,3,2,1]])
>>> [9,[8,7,6,5,4,3,2,1]]

string = '455532123266'
print(numbers_in_string( [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]])
>>> [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]

string = '123456789'
print(numbers_in_string([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Inputs
* String of numbers from 1-9

## Outputs
* List of integers

## Human Method
Read through string one by one. If item is <= to the previous, add to sub list. If item in sub list is greater than previous number not in sublist. Repeat until end of string.

## Refined
* Loop through input string
* Convert each item to integer
* Track previous item and compare
* If smaller than previous, add to sub-list
* Add to sublist until greater than previous
* Add to inital level of list

