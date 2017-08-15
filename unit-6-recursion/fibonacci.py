# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)


def fibonacci(n):
    """ Calculates fibonacci number up to n

    Recursive, only low fibonaccci numbers can be
    calculated without memoization.

    Args:
        n (int): Fibonacci number to calculate
    Returns:
        Int: nth fibonacci number
    """
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_iterative(n):
    """ Calculates fibonacci number up to n

    Non-recursive, allows much higher numbers to be
    calculated without memoization.

    Args:
        n (int): Fibonacci number to calculate
    Returns:
        Int: nth fibonacci number
    """
    # Base cases
    if n == 0 or n == 1:
        return n

    result = 0
    prev2 = 0  # Two 'steps' before
    prev1 = 1  # One 'step' before
    i = 2  # First 2 values (0,1) handled by base case

    while i <= n:
        result = prev2 + prev1
        prev2 = prev1
        prev1 = result
        i += 1
    return result


print(fibonacci(0))
#>>> 0
print(fibonacci(1))
#>>> 1
print(fibonacci(15))
#>>> 610

print(fibonacci_iterative(0))
#>>> 0
print(fibonacci_iterative(36))
#>>> 14930352
