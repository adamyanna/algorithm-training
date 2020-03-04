#
# @lc app=leetcode.cn id=54 lang=python
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        # 模拟旋转
        # TODO

        result = []
        while matrix:
            if not result:
                result = matrix.pop(0)
            else:
                result.extend(matrix.pop(0))
            if not matrix: return result
            for s in range(len(matrix)):
                result.append(matrix[s][-1])
                matrix[s].pop(-1)
            for _ in range(len(matrix[-1])):
                result.append(matrix[-1][-1])
                matrix[-1].pop(-1)

            while matrix and not matrix[-1]:
                matrix.pop(-1)
            for j in range(len(matrix)):
                result.append(matrix[len(matrix) - 1 - j][0])
                matrix[len(matrix) - 1 - j].pop(0)
                
            while matrix and not matrix[-1]:
                matrix.pop(-1)
        return result


# @lc code=end

