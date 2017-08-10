# Symmetric Square
A list  is symmetric if the first row is the same as the first column, the second row is the same as the second column etc…
Write a function to determine whether a list is symmetric.

## Example input and output:
```
print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
>>> True

print symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "fish"],
               ["fish", "fish", "cat"]])
>>> True
```

## Inputs
* 2D List -> Any type: int, str etc

## Outputs:
* Boolean: True if symmetric False if not

## Human Method
Check first row against first column, check second row against second column, repeat until row/column don't match or end of list.

### Psuedocode
```
For i in len(list):
    Get row[i]
    Get column[i]
    If row != column:
        Return False
Return True
```
## Refine
1. Get first item of first row `list[0][0]`
2. Compare to first item of first column `list[0][0]`
3. Get second item of first row `list[0][1]`
4. Compare to second item of first column `list[1][0]`
5. Get third item of first row `list[0][2]`
6. Compare to third item of first column `list[2][0]`
7. Repeat

**Alternating Iterators** betwwen column and row -> row = `list[i][j]`, col = `list[j][i]`.

### Psuedocode
```
For i -> len(list):
	for j -> len(list[i]):
        row_item = list[i][j]
        col_item = list [j][i]

        if row_item != col_item:
            return False
return True
```
* Cases to handle:
    * Empty list
    * Length of row != column length (length of outer list) and row length changing
        * Would result in index out of bound error at runtime
     