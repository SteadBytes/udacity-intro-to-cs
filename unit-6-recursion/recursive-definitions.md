# Recursive Definitions
Two parts:
1. Base case - a starting point
    * Not defined in terms of itself,
    * Smallest input - already know how to define.
    * Don't need any computation to get answer.
2. Recursive Case
    * Defined in terms of "smaller" version of itself.

## Defining Procedures Recursively
### Factorial Definition
`factorial(n) = n * (n-1) * (n-2)* ... *1`

Not a good definition becuase of the **"..."**. Humans can understand what it implies, but **computers cannot**.

### Factorial **Recursive** Definition
Base Case:
* `factorial(0) = 1`

Recursive Case:
* `factorial(n) = n*factorial(n-1)` where `n > 0`

### Code
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


```