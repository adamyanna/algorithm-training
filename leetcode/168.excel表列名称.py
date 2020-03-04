#
# @lc app=leetcode.cn id=168 lang=python
#
# [168] Excel表列名称
#

# @lc code=start
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        # 做反了
        # l = len(n)
        # s = 0
        # for i in range(l):
        #     s += (ord(v) - 97 - 1) * (26 ** (l-1-i))

        # return s

        r = ""
        while n > 0:
            if n <= 26: 
                if n > 0: r = chr(n + (65-1)) + r
                return r
            m = n%26
            if m == 0 and n > 26:
                m = 26
                n -= m
            n = n/26
            if m > 0: r = chr(m + (65-1)) + r
            

# @lc code=end

