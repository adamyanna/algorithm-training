#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        if not intervals: return []
        intervals.sort(key=lambda x: x[0])
        result = []
        tmp = intervals[0]
        for v in intervals:
            if tmp[0] <= v[0] <= tmp[1]:
                tmp[1] = max(tmp[1], v[1])
            else:
                result.append(tmp)
                tmp = v
        result.append(tmp)

        return result

        
# @lc code=end

