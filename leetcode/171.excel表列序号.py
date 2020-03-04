#
# @lc app=leetcode.cn id=171 lang=python
#
# [171] Excel表列序号
#

# @lc code=start
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        r = 0
        for i in range(l):
            r += (ord(s[i]) - 65 + 1) * (26 ** (l-1-i))

        return r

# @lc code=end

