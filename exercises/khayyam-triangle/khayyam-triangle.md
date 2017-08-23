# Khayyam Triangle
The French mathematician, Blaise Pascal, who built a mechanical computer in
the 17th century, studied a pattern of numbers now commonly known in parts of
the world as **Pascal's Triangle** (it was also previously studied by many Indian,
Chinese, and Persian mathematicians, and is known by different names in other
parts of the world).

The pattern is shown below:
```
    1           
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
   ...      
```
Each number is the **sum of the number above it to the left and the number above
it to the right** (any missing numbers are counted as 0).

## Problem
Define a procedure, `triangle(n)`, that takes a number n as its input, and
returns a list of the first n rows in the triangle. Each element of the
returned list should be a list of the numbers at the corresponding row in the
triangle.
## Inputs
* *n* = Integer, number of Pascal Triangle rows to return.
## Outputs
* List of first *n* rows of triangle
    * Each element should be a list of the numebrs in that row.
## Example:
```python
print(triangle(5))
# >>>[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]] 
```