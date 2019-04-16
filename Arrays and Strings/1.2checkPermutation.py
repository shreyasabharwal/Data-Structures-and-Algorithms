'''
1.2 Check Permutation: Given two strings , write a method to decide if one is a permutation of the other.
'''

'''
Ask the interviewer is permutation comparison is case-senstive. Additionally ask if whitespaces are significant.
'''
import sys


def check_permutation(str1, str2):
    '''Checking if the two strings have identical character counts; incrementing character counts in one loop and decrementing in the other'''

    # assuming permutation is case-sensitive and whitespaces are significant

    if len(str1) != len(str2):
        return False

    dict_chars = {}
    for char in str1:
        if char in dict_chars:
            dict_chars[char] += 1
        else:
            dict_chars[char] = 1

    for char in str2:
        if char in dict_chars:
            dict_chars[char] -= 1
        else:
            return False

    values = list(dict_chars.values())
    return (all(v == 0 for v in values))
# Time Complexity: O(n); space complexity: O(1)


if __name__ == "__main__":
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    print(check_permutation(str1, str2))
