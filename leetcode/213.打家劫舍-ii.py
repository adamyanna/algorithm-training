#
# @lc app=leetcode.cn id=213 lang=python
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 本题使用动态规划
        # 1. dp状态定义， 将nums中的到当前天的最大金额为dp[i]
        # 2. 根据要求，不能连续获取数字，可以相隔1到n-2个房间获取，还需要考虑条件为当前所考虑的元素不是末尾元素
        #   if i < len(nums) - 1: dp[i] = max[dp[i-1], dp[i-2] + nums[i]], 
        #   else: dp[i] = max[dp[i-1], dp[i-2] + nums[i] - dp[0]], 
        # ex:  6 2 3 10 15  dp = [6, 6, 6 + 3, 10 + 6, 15+9-6]


        # 此类问题的统一解决方法

        if not nums: return 0
        if len(nums) <= 3: return max(nums)
        dp = [0]*len(nums)
        dp_max = 0
        for j in (0, 1):
            for i in range(j, len(nums)-1+j):
                k = j + i if j == 1 else j+1
                dp[i] = max(dp[i-1], dp[i-2] + nums[i]) if i > j+1 else max(nums[j:k])
                dp_max = max(dp_max, dp[i])
            dp = [0]*len(nums)
        
        return dp_max







# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""