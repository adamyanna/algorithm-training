#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # BFS 2**i 对称

        print root

        queue = [root]
        level = 0
        last_null = 0
        current_null = 0
        while queue and root:
            if len(queue) == 2**level - last_null * 2:
                last_null = last_null * 2 + current_null
                current_null = 0
                # if level > 1 and len(queue) % 2 != 0:
                #     return False
                i,j = -1, len(queue)
                print [v.val if v else None for v in queue]
                while i < j:
                    i += 1
                    j -= 1
                    if level > 0 and i == j:
                        return False
                    if queue[i] == queue[j] == None:
                        continue
                    if not queue[i] or not queue[j] or queue[i].val != queue[j].val:
                        return False
                level += 1
                t_q = []
                for v in queue:
                    if v: t_q.append(v)
                queue = t_q
                if not queue:
                    break
            node = queue.pop(0)
            if not node:
                continue
            if node.left:
                queue.append(node.left)
            else:
                queue.append(None)
                current_null += 1
            if node.right:
                queue.append(node.right)
            else:
                queue.append(None)
                current_null += 1
        
        print root

        if root and ((not root.left and root.right) or (not root.right and root.left)): return False
        return True


    #     class Solution {
    # public boolean isSymmetric(TreeNode root) {
    #     return isMirror(root, root);
    # }

#     public boolean isMirror(TreeNode t1, TreeNode t2) {
#         if (t1 == null && t2 == null) return true;
#         if (t1 == null || t2 == null) return false;
#         return (t1.val == t2.val)
#             && isMirror(t1.right, t2.left)
#             && isMirror(t1.left, t2.right);
#     }
# }

        
        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/5_tree
"""