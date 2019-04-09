"""Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_nums = {}
        for i in range(len(nums)):
            if nums[i] not in dict_nums:
                dict_nums[nums[i]] = 1
            else:
                dict_nums[nums[i]] = dict_nums[nums[i]]+1

        max_key = max(dict_nums, key=dict_nums.get)
        return (max_key)
