#
# @lc app=leetcode.cn id=387 lang=python
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 一次遍历该数组

        result = {}
        p = []
        for i in range(len(s)):
            if s[i] not in p:
                p.append(s[i])
                result.update({s[i]: i})
            else:
                if s[i] in result.keys(): result.pop(s[i])
        if not result:
            return -1
        else:
            for v in p:
                if v in result.keys(): return result[v]

        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""