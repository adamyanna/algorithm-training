#
# @lc app=leetcode.cn id=124 lang=python
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import sys
        self.max_sum = - sys.maxint - 1
        def max_gain(node):
            if not node:
                return 0

            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # the price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain
            
            # update max_sum if it's better to start a new path
            self.max_sum = max(self.max_sum, price_newpath)
        
            # for recursion :
            # return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)
   
        max_gain(root)
        return self.max_sum
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/5_tree
"""