'''136. Single Number: Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?'''

'''Concept

If we take XOR of zero and some bit, it will return that bit
a xor 0 = a
If we take XOR of two same bits, it will return 0
a xor a = 0
a xor (b xor a) = (a xor a) xor b = 0 xor b = b
So we can XOR all bits together to find the unique number.'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # using bit manipulation
        uniqueInt = 0
        for i in range(len(nums)):
            uniqueInt ^= nums[i]
        return uniqueInt
