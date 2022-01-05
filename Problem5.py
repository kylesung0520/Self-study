#leetcode problem

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        retVal = []

        for x in range(len(nums)-1):
            for y in range(x+1, len(nums)):
                if nums[x] + nums[y] == target:
                    retVal = [x,y]

        return retVal

#Solved this problem using brute force algo with O(n^2) time complexity and O(1) space complexity
#But it can be solved by using two hash map with O(n) time complexity but O(n) space complexity