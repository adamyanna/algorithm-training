#
# @lc app=leetcode.cn id=319 lang=python
#
# [319] 灯泡开关
#

# @lc code=start
import math

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        light = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if i*i > n:
                break
            light += 1
        return light


        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""