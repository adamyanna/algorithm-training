#
# @lc app=leetcode.cn id=419 lang=python
#
# [419] 甲板上的战舰
#

# @lc code=start
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    if (i > 0 and board[i - 1][j] == "X") or (j > 0 and board[i][j - 1] == "X"):
                        continue
                    count += 1
        return count
        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""