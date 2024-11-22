#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start=0):
            if start == n:
                result.append(nums[:])
            for i in range(start, n):
                if i != start and nums[i] == nums[start]:
                    continue
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start + 1)
                nums[i], nums[start] = nums[start], nums[i]

        nums.sort()
        n = len(nums)
        result = []
        backtrack()
        return result
        
        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/5_back_tracking
"""