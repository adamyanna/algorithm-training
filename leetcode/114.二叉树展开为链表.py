#
# @lc app=leetcode.cn id=114 lang=python
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 94题 mirrors

        # 原地算法，直接将所有值接到节点的右子树

        # 使用后序遍历
        #     1
        #    / \
        #   2   5
        #  / \   \
        # 3   4   6

        #     1
        #    / \
        #   2   5
        #    \   \
        #     3   6
        #      \
        #       4

        # 1
        #  \
        #   2
        #    \
        #     3
        #      \
        #       4
        #        \
        #         5
        #          \
        #           6
        # 使用后续遍历，将第一个找到的右子树改为第一个找到的左子树的右孩子
        # 并递归活迭代

        # 递归

        # 改变方向的从右向左的后序遍历
        self.last_right = None # 上一个已经排到右边的节点，活着说上个已经完成转链表的节点
        def recursive_post(node):
            if not node: return
            recursive_post(node.right)
            recursive_post(node.left)
            node.right = self.last_right
            node.left = None
            self.last_right = node
        
        return recursive_post(root)


        # public void flatten(TreeNode root) { 
        #     Stack<TreeNode> toVisit = new Stack<>();
        #     TreeNode cur = root;
        #     TreeNode pre = null;

        #     while (cur != null || !toVisit.isEmpty()) {
        #         while (cur != null) {
        #             toVisit.push(cur); // 添加根节点
        #             cur = cur.right; // 递归添加右节点
        #         }
        #         cur = toVisit.peek(); // 已经访问到最右的节点了
        #         // 在不存在左节点或者右节点已经访问过的情况下，访问根节点
        #         if (cur.left == null || cur.left == pre) {
        #             toVisit.pop(); 
        #             /**************修改的地方***************/
        #             cur.right = pre;
        #             cur.left = null;
        #             /*************************************/
        #             pre = cur;
        #             cur = null;
        #         } else {
        #             cur = cur.left; // 左节点还没有访问过就先访问左节点
        #         }
        #     } 
        # }

        # de = [(root, sum - root.val), ]
        # while de:
        #     node, curr_sum = de.pop()
        #     if not node.left and not node.right and curr_sum == 0:  
        #         return True
        #     if node.right:
        #         de.append((node.right, curr_sum - node.right.val))
        #     if node.left:
        #         de.append((node.left, curr_sum - node.left.val))
        # return False

    
        
# @lc code=end

