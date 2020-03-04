#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 在不使用递归的方式的情况下，使用栈来记录数据，完成中序
        # public class Solution {
        #     public List < Integer > inorderTraversal(TreeNode root) {
        #     List < Integer > res = new ArrayList < > ();
        #     Stack < TreeNode > stack = new Stack < > ();
        #     TreeNode curr = root;
        #     while (curr != null || !stack.isEmpty()) {
        #         while (curr != null) {
        #             stack.push(curr);
        #             curr = curr.left;
        #         }
        #         curr = stack.pop();
        #         res.add(curr.val);
        #         curr = curr.right;
        #     }
        #     return res;
        # }
        # 递归的方式
        # class Solution {
        #     public List < Integer > inorderTraversal(TreeNode root) {
        #         List < Integer > res = new ArrayList < > ();
        #         helper(root, res);
        #         return res;
        #     }

        #     public void helper(TreeNode root, List < Integer > res) {
        #         if (root != null) {
        #             if (root.left != null) {
        #                 helper(root.left, res);
        #             }
        #             res.add(root.val);
        #             if (root.right != null) {
        #                 helper(root.right, res);
        #             }
        #         }
        #     }
        # }
        #时间复杂度：O(n)O(n)。递归函数 T(n)=2⋅T(n/2)+1T(n)=2⋅T(n/2)+1。
        #    空间复杂度：最坏情况下需要空间O(n)O(n)，平均情况为O(log⁡n)O(logn)。
 

        stack = []
        result = []
        current = root
        while current or stack:
            # 找到当前节点的最左
            while current:
                stack.append(current)
                current = current.left
            # 当前节点的最左应该是遍历的第一个值
            # 外层循环将没有找到right的节点,将继续吧目标值更新为栈顶的值
            current = stack.pop(-1)
            result.append(current.val)
            # 寻找当前节点的第一个right，找到right后再对right做同样的一直找左子树的操作
            current = current.right
        return result

        # 时间复杂度： 假设结果长度为n，那么时间复杂度为n  空间复杂度 n


        # def middle(node, res):
        #     if node:
        #         print res
        #         if node.left: middle(node.left, res)
        #         res.append(node.val)
        #         if node.right: middle(node.right, res)
        #         return True
        
        # res = []
        # middle(root, res)
        # return res



# @lc code=end

