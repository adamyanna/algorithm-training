#
# @lc app=leetcode.cn id=116 lang=python
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        # 层序遍历，从最下层往最上层

        queue = [root]
        level = 0
        last_null = 0
        current_null = 0
        left_node = None
        while queue and root:
            if len(queue) == 2**level - last_null * 2 - current_null:
                last_null = last_null * 2 + current_null
                current_null = 0
                level += 1
                
                # 完全二叉树，不用考虑缺少的左右子树，所以可以忽略last_null和current_null
                for i in range(len(queue)-1):
                    queue[i].next = queue[i+1]
                left_node = queue[0]
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            else:
                current_null += 1
            if node.right:
                queue.append(node.right)
            else:
                current_null += 1
            node.right = None
            if node != left_node: node.left = None

        return root
        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/5_tree
"""