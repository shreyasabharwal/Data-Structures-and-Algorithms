'''
1.3 URLify: Write a method to replace all spaces in a string with "%20". You may assume that the string
    has sufficient space at the end to hold the additional characters, and that you are given the "true"
    length of the string.

EXAMPLE
Input: "Mr John Smith JJ, 13
Output: "Mr%2eJohn%2eSmith"
'''

''' A common approach in string manipulation problems is to edit the string starting from the end and working
backwards. This is useful because we have an extra buffer at the end, which allows us to change characters
without worrying about what we're overwriting.
Since python strings are immutable, the string is converted to a list first to avoid creating a new copy of the String.
'''


import sys


def urlify(string, orig_length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    new_index = len(string)
    for i in reversed(range(orig_length)):
        if string[i] == ' ':
            string[new_index-3:new_index] = '%20'
            new_index -= 3
        else:
            string[new_index-1] = string[i]
            new_index -= 1
    return ''.join(string)


if __name__ == "__main__":
    # converting string to list
    string = list(input("enter a string"))
    # original length of the string without trailing spaces
    orig_length = int(input("enter length"))
    print(urlify(string, orig_length))

# Time Complexity = O(n)
