#
# @lc app=leetcode.cn id=48 lang=python
#
# [48] 旋转图像
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # TODO finish my version
        # tmp = []
        # size = len(matrix)
        # i = 0
        # while i < size/2:
        #     tmp = matrix[i]

        n = len(matrix[0])        
        for i in range(n / 2 + n % 2):
            for j in range(n / 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp

        
        
# @lc code=end

