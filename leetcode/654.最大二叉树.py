#
# @lc app=leetcode.cn id=654 lang=python
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.construct(nums, 0, len(nums))


    def construct(self, eles, l, r):
        if l == r:
            return
        value, max_index = self.find_max(eles, l, r)
        node = TreeNode(value)
        node.left = self.construct(eles, l, max_index)
        node.right = self.construct(eles, max_index + 1, r)
        return node

    def find_max(self, input, begin, end):
        max_v, max_i = 0, begin
        for i in range(begin, end):
            if input[i] > max_v:
                max_v = input[i]
                max_i = i
        return max_v, max_i


        
# @lc code=end

