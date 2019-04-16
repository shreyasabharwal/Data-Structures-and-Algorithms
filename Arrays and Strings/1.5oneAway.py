'''
1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
    remove a character, or replace a character. Given two strings, write a function to check if they are
    one edit (or zero edits) away.

EXAMPLE
pale, ple -) true
pales, pale -) true
pale, bale -) true
pale, bae -) false
'''


def one_away(str1, str2):
    dict_chars = {}
    if abs(len(str1)-len(str2)) > 1:
        return False

    for char in str1:
        if char in dict_chars:
            dict_chars[char] += 1
        else:
            dict_chars[char] = 1

    for char in str2:
        if char in dict_chars:
            dict_chars[char] -= 1
        else:
            dict_chars[char] = 1

    count = 0
    for v in dict_chars.values():
        if v == 1:
            count += 1
    # count=0 if zero edits, count=1 if insert/remove edit, count=2 if replace edit
    if(count > 2):
        return False
    return True


if __name__ == "__main__":
    str1 = input("enter 1st string:")
    str2 = input("enter 2nd string:")
    print(one_away(str1, str2))

# Time complexity: O(n)
