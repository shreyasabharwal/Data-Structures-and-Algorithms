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
        max_current, max_global = nums[0], nums[0]
        for i in range(1, len(nums)):
            max_current = max(max_current + nums[i], nums[i])
            if max_global < max_current:
                max_global = max_current
            print(i, max_current, max_global)
        return max_global
