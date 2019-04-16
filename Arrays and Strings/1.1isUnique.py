
'''
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. 
    What if you cannot use additional data structures
'''

'''
Ask the interviewer if the string is ASCII(128 characters) or unicode or extended ASCII(256 characters).
'''


def is_unique(string):
    """Using hast table to check if all characters have a count of one"""
    # if string is ASCII
    if len(st) > 128:
        return False
    dict_chars = {}
    for char in string:
        if char in dict_chars:
            return False
        else:
            dict_chars[char] = 1
    return True
# Time Complexity: O(n); Space Complexity: O(1)

# without using additional data structures


def is_unique_1(string):
    """Sorting the string and checking if neighboring elements have repeated characters"""
    # if string is ASCII
    if len(string) > 128:
        return False
    string = ''.join(sorted(string))
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return False
    return True
# Time Complexity: O(nlogn);


if __name__ == "__main__":
    st = input("enter a string:")
    print(is_unique(st))
