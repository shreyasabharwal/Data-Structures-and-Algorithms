'''242. Valid Anagram

Given two strings s and t, write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?'''


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # using hash table
        dict_counts = {}

        if len(s) != len(t):
            return False

        for string in s:
            if string in dict_counts:
                dict_counts[string] += 1
            else:
                dict_counts[string] = 1

        for string in t:
            if string in dict_counts:
                dict_counts[string] -= 1
            if string not in dict_counts or dict_counts[string] < 0:
                return False

        return True
