'''
1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a substring
    of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
    call to isSubstring(e.g., "waterbottle" is a rotation "erbottlewat").
'''


def isSubstring(string, substring):
    if substring in string:
        return True
    else:
        return False

# s2 will always be a substring of s1+s1


def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    new_str = s1+s1
    return (isSubstring(new_str, s2))


if __name__ == "__main__":
    s1 = input("enter 1st string:")
    s2 = input("enter 2nd string:")
    print(string_rotation(s1, s2))
