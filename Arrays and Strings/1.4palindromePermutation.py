'''
1.4: Palindrome Permutation: Given a string, write a function to check if it is a permutation of
    a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
    permutation is a rearrangement of letters. The palindrome does not need to be limited to just
    dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations:"taco cat'; "atco cta'; etc.)
'''

'''
Ask the interviewer if the strings comparison is case-sensitive
'''


def panlindrome_permutation(string):
    '''checking the counts of all characters. All but one should have an even count. The remaining one can be even or odd'''
    dict_chars = {}
    for char in string:
        if char == ' ':
            continue
        elif char in dict_chars:
            dict_chars[char] += 1
        else:
            dict_chars[char] = 1

    count = 0
    for k, v in dict_chars.items():
        if v % 2 != 0:
            count += 1

    if count > 1:
        return False
    return True


if __name__ == "__main__":
    string = input("enter a string:")
    print(panlindrome_permutation(string))

# Time Complexity: O(n)
