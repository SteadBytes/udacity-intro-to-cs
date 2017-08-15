def rabbits(n):
    if n < 0:
        # when n < 5, (n-5) is negative
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        # rabbits(n-5) = 0 when n < 5
        return rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)


# Test cases
print(rabbits(10))
#>>> 35

s = ""
for i in range(1, 12):
    s = s + str(rabbits(i)) + " "
print(s)
#>>> 1 1 2 3 5 7 11 16 24 35 52
