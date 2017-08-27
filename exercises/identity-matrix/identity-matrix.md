# Identity Matrix
An IDENTITY matrix is a **square** matrix in which all the elements 
on the principal/main diagonal are 1 and all the elements outside 
the principal diagonal are 0. 

## Problem
Given a list of lists representing a n * n matrix as input, define a  procedure that returns True if the input is an identity matrix and False otherwise.

## Example input and output:
```
matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)
>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)
>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)
>>>False
```
## Inputs
* Square matrix (2d List) of integers.

## Outputs
* Boolean: True if identity matrix False if not

## Human Method
Check that primary diagonal consists only of 1's. Then check around the primary diagonal and ensure only 0's are present

```
Check first diagonal item -> matrix[0][0]
Check second diagonal item -> matrix[1][1]
Check third diagonal item -> matrix [2][2]
Repeat until len(matrix) reached.
Loop through other elements, check if 0
```
**Iterators are equal on diagonals**

## Refine
* Use **two loops** to traverse matrix (one inner, one outer).
* Each element must = 0 **unless both iterators are equal**.

### Pseudocode
```
for i -> len(matrix):
    for j -> len(matrix[i]):
        if i == j:
            if current_item != 1:
                return False
        else:
            if current_item != 0:
                return False
    return True

```
* Cases to handle:
    * Empty list
    * Length of list <=1
