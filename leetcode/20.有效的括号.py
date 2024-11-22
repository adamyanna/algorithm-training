#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 1. from 0 to n > and find it's pair X
        # 1. L, R
        # 2. 1,2,3 reverse 3,2,1

        stack = []
        q_dict = {
            "(": (1, "L"),
            ")": (1, "R"),
            "[": (2, "L"),
            "]": (2, "R"),
            "{": (3, "L"),
            "}": (3, "R")
        }
        for v in s:
            if q_dict[v][1] == "R":
                if not stack:
                    return False
                else:
                    if q_dict[v][0] == stack[-1:][0][0]:
                        stack.pop(len(stack) - 1)
                    else:
                        return False
            else:
                stack.append(q_dict[v])
        if not stack:
            return True
        return False


# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/2_stack
"""