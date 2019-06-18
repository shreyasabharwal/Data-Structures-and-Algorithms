'''125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false'''


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = "".join(char for char in s if char.isalnum())

        j = len(new_s)-1
        for i in range(len(new_s)//2):
            if new_s[i].lower() != new_s[j].lower():
                return False
            j -= 1

        return True
