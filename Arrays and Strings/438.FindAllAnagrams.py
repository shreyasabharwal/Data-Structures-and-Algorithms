'''438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20, 100.
The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

'''

'''
Used hash tables and sliding window concept
'''


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        d_counts_fixed, d_counts = [0]*127, [0]*127
        res = []

        for pchar in p:
            d_counts_fixed[ord(pchar)] += 1

        for char in s[:len(p)]:
            d_counts[ord(char)] += 1

        if d_counts == d_counts_fixed:
            res.append(0)

        for i in range(1, len(s)-len(p)+1):
            d_counts[ord(s[i-1])] -= 1
            d_counts[ord(s[i-1+len(p)])] += 1
            if d_counts == d_counts_fixed:
                res.append(i)

        return res
