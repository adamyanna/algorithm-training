#
# @lc app=leetcode.cn id=268 lang=python
#
# [268] 缺失数字
#

# @lc code=start
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 位运算
        # 异或，两个相同的数异或得到的结果为0
        miss_n = len(nums)
        for i in range(len(nums)):
            miss_n ^= i ^ nums[i]
        return miss_n

        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""