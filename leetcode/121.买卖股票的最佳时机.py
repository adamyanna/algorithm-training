#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#
import sys
# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # 动态规划
        # 状态转移方程
        # int n = prices.length;
        # int[][] dp = new int[n][2];
        # for (int i = 0; i < n; i++) {
        #     dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]);
        #     dp[i][1] = Math.max(dp[i-1][1], -prices[i]);
        # }
        # return dp[n - 1][0];

        max_pro = 0
        min_pri = sys.maxint
        for v in prices:
            min_pri = min(v, min_pri)
            max_pro = max(max_pro, v - min_pri)

        return max_pro

        
# @lc code=end

