#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#
import sys
# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 贪心
        # 滑动窗口
        # 分治


        window = 0
        result_max = - sys.maxint -1
        for v in nums:
            window += v
            window = max(window, v)
            result_max = max(window, result_max)
            
        return result_max

                    
            
        
# @lc code=end

