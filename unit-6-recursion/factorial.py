# Define a procedure, factorial, that takes a natural number as its input, and
# returns the number of ways to arrange the input number of items.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_iterative(n):
    product = 1
    for i in range(0, n + 1):
        product *= i
    return product


print(factorial(0))
#>>> 1

print(factorial(5))
#>>> 120

print(factorial(10))
#>>> 3628800

print(factorial_iterative(0))
#>>> 1

print(factorial_iterative(5))
#>>> 120

print(factorial_iterative(10))
#>>> 3628800
