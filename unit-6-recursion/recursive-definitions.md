# Recursive Definitions
Two parts:
1. Base case - a starting point
    * Not defined in terms of itself,
    * Smallest input - already know how to define.
    * Don't need any computation to get answer.
2. Recursive Case
    * Defined in terms of "smaller" version of itself.

**Without** a base case, it is a **circular definition**.

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

## Recursion vs Iteration
**Anything** that can be defined recursively can also be defined iteratively. Recursion can be very expensive computationally. Some languages are better than other for recursion - Python is not very good.

### Iterative Factorial
```python
def factorial_iterative(n):
    product = 1
    for (i in range(0,n+1))
        product *= i
    return product
```