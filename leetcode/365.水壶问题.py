#
# @lc app=leetcode.cn id=365 lang=python
#
# [365] 水壶问题
#

# @lc code=start
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """

        # 裴蜀定理
        # 求解最大公约数问题

        def _gcd(x, y):
            if y == 0: return x
            z = x % y
            return _gcd(y, z)

        if (x == y != z and z!= 0) or (z > x + y): return False
        if z == 0 or z % _gcd(x, y) == 0: return True




# @lc code=end

