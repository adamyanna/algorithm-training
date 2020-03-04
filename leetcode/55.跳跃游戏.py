#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # l = len(nums)
        # if l == 1:
        #     return True
        # for i in range(0, l):
        #     if i != l - 1 and nums[i] == 0:
        #         return False
        #     max_step = i + nums[i]
        #     while i < max_step and i < l - 1:
        #         i += 1
        #         if nums[i] != 0:
        #             break
        #     if i >= l - 1:
        #         return True
            # if i > l -1:
            #     return False
        # 题目中指出数组中的元素代表能跳跃的最大长度  最大 最大 最大

        # 动态规划，自底向上，自顶向下


        # 贪心

        l = len(nums)
        position = l - 1
        if l == 1:
            return True
        for i in range(1, l):
            j = l - 1 - i
            if j + nums[j] >= position:
                position = j
        
        if position == 0:
            return True
        else:
            return False
        
# @lc code=end

