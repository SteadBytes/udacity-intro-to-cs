# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible
# algorithm or even language of the clear text message, one could perform
# frequency analysis. This process could be described as simply counting
# the number of times a certain symbol occurs in the given text.
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains
# the lowercase letters a-z.
# As output you should return a list of the normalized frequency
# for each of the letters a-z.
# The normalized frequency is simply the number of occurrences, i,
# divided by the total number of characters in the message, n.


def freq_analysis(message):
    """ Returns a normalized frequency analysis of an input string.

    Frequency of each letter a-z is tracked, then divided by length of input to normalize

    Args:
        message: String of lowercase a-z characters
    Returns:
        List of (float) normalized frequencies for each letter in the input string
    """
    # Each element of array represents a letter
    # i.e. index 0 = a, index 1 = b
    letter_counts = [0] * 26
    for i in message:
        # ASCII for lowercase starts at 97
        pos = ord(i) - 97
        letter_counts[pos] += 1
    return [float(x) / len(message) for x in letter_counts]


# Tests


print(freq_analysis("abcd"))
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print(freq_analysis("adca"))
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print(freq_analysis('bewarethebunnies'))
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]
