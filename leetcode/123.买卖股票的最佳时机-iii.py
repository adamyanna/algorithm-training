#
# @lc app=leetcode.cn id=123 lang=python
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Solution:
        # 定义4个变量
        #
        # 比较为 3个数中留下最大的两个
        fst_lower, sec_lower, fst_max, sec_max = sys.maxint, sys.maxint, 0, 0

        res_max = 0

        for i in xrange(len(prices)):
            if prices[i] < fst_lower:
                fst_lower = prices[i]
            if prices[i] - fst_lower > fst_max:
                fst_max = prices[i] - fst_lower

            res_max = fst_max
            if i < len(prices) - 1 and prices[i + 1] < prices[i]:
                res_max += prices[i] - prices[i - 1]

        return res_max

        # for i in prices:
        #     if i < fst_lower:
        #         fst_lower = i
        #     if i - fst_lower > fst_max:
        #         fst_max = i - fst_lower

        #     if i - fst_max < sec_lower:
        #         sec_lower = i - fst_max
        #     if i - sec_lower > sec_max:
        #         sec_max = i - sec_lower

        # return sec_max

        # p = []

        # for i in xrange(len(prices)):

        #     if prices[i] < fst_lower:
        #         fst_lower = prices[i]
        #         if fst_max:
        #             p.append(fst_max)
        #         if len(p) == 2:
        #             if fst_max > p[0] and p[0] < p[1]:
        #                 p.pop(0)
        #                 p.append(fst_max)
        #             if fst_max > p[1] and p[1] < p[0]:
        #                 p.pop(1)
        #                 p.append(fst_max)
        #         fst_max= 0

            
        #     if prices[i] - fst_lower > fst_max:
        #         fst_max = prices[i] - fst_lower
        #         if i + 1 > len(prices) - 1 and p:
        #             p.append(fst_max)

        #     if i + 1 > len(prices) - 1:
        #         if not p:
        #             return fst_max
        #         elif len(p) == 1:
        #             return p[0]
        #         elif len(p) == 2:
        #             return p[0] + p[1]

        # return 0
            
        
# @lc code=end
