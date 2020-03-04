#
# @lc app=leetcode.cn id=165 lang=python
#
# [165] 比较版本号
#

# @lc code=start
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        # 最简单的方式就是 将字符串用.分割成数组，然后用int比较, 不需要使用lstrip
            #         v1, v2 = 0, 0
            # if i < len(l1): v1 = int(l1[i].lstrip("0")) if l1[i].lstrip("0") else 0
            # if i < len(l2): v2 = int(l2[i].lstrip("0")) if l2[i].lstrip("0") else 0
        l1 = version1.split(".")
        l2 = version2.split(".")
        i = 0
        while i < max(len(l1), len(l2)):
            v1, v2 = 0, 0
            if i < len(l1): v1 = int(l1[i])
            if i < len(l2): v2 = int(l2[i])
            i += 1
            if v1 == v2:
                continue
            elif v1 > v2:
                return 1
            else:
                return -1

        return 0

            



# @lc code=end

