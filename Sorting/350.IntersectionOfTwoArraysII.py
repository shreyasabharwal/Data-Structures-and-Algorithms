'''350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2, 2]

Example 2:
Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Output: [4, 9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # unsorted - Time Complexity: O(n1), space complexity: O(n2)
        if len(nums1) < len(nums2):
            self.intersect(nums2, nums1)

        d_nums, res = {}, []

        for num in nums2:
            if num not in d_nums:
                d_nums[num] = 1
            else:
                d_nums[num] += 1

        for num in nums1:
            if num in d_nums and d_nums[num] > 0:
                res.append(num)
                d_nums[num] -= 1

        return res

    def intersectSorted(self, nums1, nums2):
        """ Follow up - sorted arrays"""
        # sorted - Time complexity: O(n1), space complexity: O(1)
        res = []
        i, j = 0, 0
        while j < len(nums2) and i < len(nums1):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return res
