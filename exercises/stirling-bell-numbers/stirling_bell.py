def stirling(n, k):
    """ Calculates the Stirling number for n items partioned into k sets.
    Args:
        n (int) number of items in set
        k (int) number of sets to partition into
    Returns:
        int
    """
    if n == k:
        return 1
    if n >= k and n > 0 and k > 0:
        return k * stirling(n - 1, k) + stirling(n - 1, k - 1)
    return 0


def bell(n):
    """ Calculates the nth Bell number
    Args:
        n (int)
    Returns
        int
    """
    result = 0
    for i in range(1, n + 1):
        result += stirling(n, i)
    return result

# Test Cases


print(stirling(1, 1))
#>>> 1
print(stirling(2, 1))
#>>> 1
print(stirling(2, 2))
#>>> 1
print(stirling(2, 3))
#>>>0

print(stirling(3, 1))
#>>> 1
print(stirling(3, 2))
#>>> 3
print(stirling(3, 3))
#>>> 1

print(stirling(4, 1))
#>>> 1
print(stirling(4, 2))
#>>> 7
print(stirling(4, 3))
#>>> 6
print(stirling(4, 4))
#>>> 1

print(stirling(5, 1))
#>>> 1
print(stirling(5, 2))
#>>> 15
print(stirling(5, 3))
#>>> 25
print(stirling(5, 4))
#>>> 10
print(stirling(5, 5))
#>>> 1

print(stirling(20, 15))
# >> > 452329200


print(bell(1))
# >>> 1
print(bell(2))
# >>> 2
print(bell(3))
# >>> 5
print(bell(4))
# >>> 15
print(bell(5))
# >>> 52
print(bell(15))
# >>> 1382958545
