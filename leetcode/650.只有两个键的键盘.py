#
# @lc app=leetcode.cn id=650 lang=python
#
# [650] 只有两个键的键盘
#

# @lc code=start
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 将一个数分解为所有因数都为素数的结果，将这些素数相加

        result = 0
        pn_start = 2
        while n > 1:
            while n%pn_start == 0:
                result += pn_start
                n /= pn_start
            pn_start += 1
        return result
        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""