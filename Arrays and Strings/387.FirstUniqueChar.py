'''387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d_counts = {}
        for char in s:
            if char in d_counts:
                d_counts[char] += 1
            else:
                d_counts[char] = 1

        for i in range(len(s)):
            if d_counts[s[i]] == 1:
                return i

        return -1
