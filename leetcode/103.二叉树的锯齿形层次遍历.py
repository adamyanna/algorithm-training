#
# @lc app=leetcode.cn id=103 lang=python
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
         # def findBottomLeftValue(self, root):
        # """
        # :type root: TreeNode
        # :rtype: int
        # """
        # # 使用队列从右往左广度优先遍历整个树，输出最后一个元素就是最后一行最左边的元素
        # queue_l = []
        # queue_l.append(root)

        # while queue_l:
        #     node = queue_l.pop(0)
        #     if node.right:
        #         queue_l.append(node.right)
        #     if node.left:
        #         queue_l.append(node.left)
        #     if not queue_l:
        #         return node.val

        # 本题解法为广度优先遍历
        # 广度优先遍历需要使用到队列
        # 如何控制分界线

        queue = [root]
        result = []
        last_null = 0
        current_null = 0
        while queue and root:
            if len(queue) == 2**len(result) - last_null * 2 - current_null:
                last_null = last_null * 2 + current_null
                current_null = 0
                if len(result) % 2 == 0:
                    result.append([n.val for n in queue])
                else:
                    j = len(queue)
                    t = []
                    while j > 0: j -= 1; t.append(queue[j].val)
                    result.append(t)
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            else:
                current_null += 1
            if node.right:
                queue.append(node.right)
            else:
                current_null += 1

        return result
        
# @lc code=end

