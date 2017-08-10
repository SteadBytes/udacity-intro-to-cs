# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.


def symmetric(list):
    if list == []:
        return True
    if len(list) != len(list[0]):
        return False
    for i in range(len(list)):
        if len(list[i]) != len(list[0]):
            return False
        for j in range(len(list[i])):
            row_item = list[i][j]
            col_item = list[j][i]
            if row_item != col_item:
                return False
    return True


print symmetric([[1, 2, 3],
                 [2, 3, 4],
                 [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "fish"],
                 ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "dog"],
                 ["fish", "fish", "cat"]])
#>>> False

print symmetric([[1, 2],
                 [2, 1]])
#>>> True

# print symmetric([[1, 2, 3, 4],
#                 [2, 3, 4, 5],
#                 [3, 4, 5, 6]])
#>>> False

print symmetric([[1, 2, 3],
                 [2, 3, 1]])
#>>> False
