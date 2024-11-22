#
# @lc app=leetcode.cn id=73 lang=python
#
# [73] 矩阵置零
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # 常数空间
        # 以第一行第一列为标记点，先判断第一行第一列的情况，记录0的数量
        # 将其他数据中的0放在第一行第一列相应位置
        # 修改全部数据
        # 1 0 0 0
        # 0 1 0 1
        # 1 1 1 1
        # 0 1 1 0

        f_row = False
        f_column = False
        if 0 in matrix[0]: f_row = True
        for i in range(len(matrix)):
            if matrix[i][0] == 0: f_column = True
        
        for m in range(1, len(matrix)):
            for n in range(1, len(matrix[0])):
                if matrix[m][n] == 0:
                    matrix[0][n] = 0
                    matrix[m][0] = 0

        for x in range(1, len(matrix)):
            if matrix[x][0] == 0:
                for t in range(1, len(matrix[x])): matrix[x][t] = 0

        for y in range(1, len(matrix[0])):
            if matrix[0][y] == 0:
                for t in range(1, len(matrix)): matrix[t][y] = 0

        if f_row:
            for t in range(0, len(matrix[0])): matrix[0][t] = 0
        
        if f_column:
            for t in range(0, len(matrix)): matrix[t][0] = 0

        return matrix

                


        
# @lc code=end

"""
类似题目：转化为全零矩阵的最少反转次数
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/7_bitwise
"""