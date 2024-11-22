#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Anylize:
        # 1. put cha and number into dict
        # 2. for the s and handle special case and get number

        result = []
        r_d = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        for i in s:
            m = 0
            if i in ["V", "X"] and result and result[len(result) - 1] == 1:
                m = 1
            elif i in ["L", "C"] and result and result[len(result) - 1] == 10:
                m = 10
            elif i in ["D", "M"] and result and result[len(result) - 1] == 100:
                m = 100
            else:
                pass
            if m != 0:
                result = result[:len(result) -1]
            v = r_d[i] - m
            result.append(v)
        sum = 0
        if not result:
            return 0
        else:
            for v in result:
                sum += int(v)
        return sum



        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/1_deterministic_finite_state_machine
"""