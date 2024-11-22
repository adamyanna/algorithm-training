#
# @lc app=leetcode.cn id=191 lang=python
#
# [191] 位1的个数
#

# @lc code=start
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n > 0:
            result += 1
            n &= n - 1
        return result
        # 对于一个二进制来说，最低位的1，
        # 一定会因为 n - 1 而变成0
        # 这时候对n和n-1做与操作，
        # 就可以得到去掉最低位1的结果
        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""