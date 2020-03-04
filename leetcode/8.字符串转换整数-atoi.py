#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=star
class Solution(object):
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        # Anylize
        #  special: return 0
        # int32
        # 

        string = string.strip()
        if not string:
            return 0
        l = [str(i) for i in xrange(10)]
        o = ["-", "+"]
        result = ""
        for v in string:
            if v in o and not result:
                result += v
            elif v in l:
                result += v
            elif not result:
                return 0
            else:
                break
        if result == "+" or result == "-":
            return 0
        if not (-2 **31 <= int(result) <= 2**31 -1):
            if int(result) < 0:
                return -2 ** 31
            else:
                return 2 ** 31 -1
        return int(result)
        
        
        
# @lc c

