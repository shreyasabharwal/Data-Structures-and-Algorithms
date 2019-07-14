
'''7. Reverse Integer

Given an integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isneg = False
        if x < 0:
            isneg = True
            x = (-1)*x
        ans = 0
        while(x != 0):
            ans = ans*10+x % 10
            print x
            x = x//10
        if isneg:
            ans = (-1)*ans
        return ans
