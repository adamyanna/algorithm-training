#
# @lc app=leetcode.cn id=452 lang=python
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        if not points:
            return 0
        points = sorted(points, key= lambda x:x[1])
        arr_n = 1
        end = points[0][1]

        for v1, v2 in points:
            if v1 > end:
                arr_n += 1
                end = v2

        return arr_n

        # 此题目 完全可以不排序
        # TODO
        # if not points:
        #     return 0
        # arr_range = [[points[0][0],points[0][1]]]
        # for v1, v2 in points:
        #     update = False
        #     for rv in arr_range:
        #         if rv[0] <= v1 <= rv[1] or rv[0] <= v2 <= rv[1] or v1 <= rv[0] <= v2 or v1 <= rv[1] <= v2:
        #             rv[0] = max(rv[0], v1)
        #             rv[1] = min(rv[1], v2)
        #             update = True
        #             break
        #     if not update: arr_range.append([v1, v2])
        # return len(arr_range)

        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""