#
# @lc app=leetcode.cn id=91 lang=python
#
# [91] 解码方法
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 动态规划，找出dp[i] dp[i-1] dp[i-2] 之间的关系
        # 1 ~ 9 
        # 10 ~ 19 
        # 20 ~ 26
        # 226
        # i = 0: dp[0] = 1
        # i = 1: dp[1] = dp[0] + (if 2 < 6)
        # i = 2: dp[2] = dp[1] + ()

        # if s[0] == "0": return 0

        # 22619
        dp = []
        for i in range(len(s)):
            if i == 0:
                if s[0] != "0":
                    dp.append(1)
                else:
                    return 0
                continue
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    if i == 1:
                        dp.append(dp[i-1])
                        continue
                    dp.append(dp[-2])
                    continue
                else:
                    return 0
            if s[i - 1] == "0":
                dp.append(dp[-1])
                continue
            if (s[i - 1] == "2" and s[i] <= "6") or (s[i - 1] == "1"):
                if i == 1:
                    dp.append(dp[i-1] + 1)
                    continue
                if dp[i -2] == "0":
                    dp.append(dp[i - 1] + 1)
                else:
                    dp.append(dp[i -1] + dp[i - 2])
            else:
                dp.append(dp[-1])
            print dp

        return dp[-1]



        
# @lc code=end

