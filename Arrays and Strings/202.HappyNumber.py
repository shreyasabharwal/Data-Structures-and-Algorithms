'''202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1'''


'''
Approach: While generating the sum of squares we will end up cycling back to a previously computed answer, and repeat the process. We create a set to keep track of previously computed answers.
'''


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        if n == 1:
            return True
        while n not in seen:
            seen.add(n)
            n = sum(int(i)**2 for i in str(n))

        if 1 in seen:
            return True
        return False
