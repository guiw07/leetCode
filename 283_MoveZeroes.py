"""
283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroPos = 0
        for pos, value in enumerate(nums):
            if nums[pos] == 0 and nums[zeroPos] != 0:
                zeroPos = pos
            if nums[pos] != 0 and nums[zeroPos] == 0:
                nums[pos], nums[zeroPos] = nums[zeroPos], nums[pos]
                zeroPos += 1