"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6

"""

# Kandan's Algorithm


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = 0
        max_so_far = nums[0]
        for i in range(len(nums)):
            sum1 = sum1 + nums[i]
            if max_so_far < sum1:
                max_so_far = sum1
            if sum1 < 0:
                sum1 = 0
        return max_so_far
