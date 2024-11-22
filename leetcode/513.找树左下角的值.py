#
# @lc app=leetcode.cn id=513 lang=python
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 使用队列从右往左广度优先遍历整个树，输出最后一个元素就是最后一行最左边的元素
        queue_l = []
        queue_l.append(root)

        while queue_l:
            node = queue_l.pop(0)
            if node.right:
                queue_l.append(node.right)
            if node.left:
                queue_l.append(node.left)
            if not queue_l:
                return node.val


        # 使用栈实现深度优先遍历

        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""