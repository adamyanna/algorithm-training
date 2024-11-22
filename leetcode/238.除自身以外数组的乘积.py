#
# @lc app=leetcode.cn id=238 lang=python
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # a1, a2,  a3,      a4
        # 1, 1*a1, 1*a1*a2, 1*a1*a2*a3

        # a1, 				a2, 		    a3, 		a4
        # a4*1*a3*a1,		a4*1*a3,		a4*1,		1

        # 由于数组是线性结构，从两端同时分别遍历，最终的即可得到答案；

        l = len(nums)
        i = 0
        j = l - 1
        result = [1]*l
        while i != l -1:
            result[i+1] = result[i] * nums[i]
            i += 1
        p = 1
        while j != 0:
            p = nums[j] * p
            result[j -1] *= p 
            j -= 1
        return result


        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""