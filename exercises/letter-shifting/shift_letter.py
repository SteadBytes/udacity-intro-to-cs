# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.


def shift(letter):
    """Returns the next letter in the alphabet, with 'a'
    following 'z'.

    Args:
        letter (char): single letter, lowercase a-z
    Return:
        Char, next letter in alphabet.
    """
    return chr((ord(letter) - ord('a') + 1) % 26 + ord('a'))


def shift_n_letters(letter, n):
    """Returns letter shifted n times into the alphabet, with 'a'
    following 'z'.

    Args:
        letter (char): single letter, lowercase a-z
        n (int): number of letters to shift by
    Return:
        Char, next letter in alphabet.
    """
    return chr((ord(letter) - ord('a') + n) % 26 + ord('a'))


def rotate(s, n):
    """Rotates a word by shifting each letter n times into the alphabet, with 'a'
    following 'z'.

    Args:
        s (string): Word/string to rotate, lowercase a-z
        n (int): number of letters to shift by
    Return:
        String, rotated string.
    """
    res = ""
    for ch in s:
        res += shift_n_letters(ch, n)
    return res


print(shift('a'))
#>>> b
print(shift('n'))
#>>> o
print(shift('z'))
#>>> a

print(shift_n_letters('s', 1))
#>>> t
print(shift_n_letters('s', 2))
#>>> u
print(shift_n_letters('s', 10))
#>>> c
print(shift_n_letters('s', -10))
#>>> i

print(rotate('sarah', 13))
#>>> 'fnenu'
print(rotate('fnenu', 13))
#>>> 'sarah'
print(rotate('dave', 5))
#>>>'ifaj'
print(rotate('ifaj', -5))
#>>>'dave'
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
              "sv rscv kf ivru kyzj"), -17))
#>>> ???
