#
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        i, c = 0, -1
        while i < len(haystack):
            if haystack[i] == needle[0] and c == -1:
                c = i
                continue
            if c != -1:
                if len(needle) > len(haystack) - c:
                    c = -1
                    break
                if i - c == len(needle):
                    break
                if haystack[i] != needle[i-c]:
                    i = c
                    c = -1
            i += 1
        return c

# @lc code=end

