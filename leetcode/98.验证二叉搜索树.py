#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 验证二叉搜索树
        # 解法：对二叉树做中序遍历，判断每次新加的值是否比前一个值大
        # 重要重要重要 ： 两个数相等也是不符合搜索二叉树的条件的


        # stack = []
        # result = []
        # current = root
        # while current or stack:
        #     # 找到当前节点的最左
        #     while current:
        #         stack.append(current)
        #         current = current.left
        #     # 当前节点的最左应该是遍历的第一个值
        #     # 外层循环将没有找到right的节点,将继续吧目标值更新为栈顶的值
        #     current = stack.pop(-1)
        #     if result and current.val <= result[-1]: return False
        #     result.append(current.val)
        #     # 寻找当前节点的第一个right，找到right后再对right做同样的一直找左子树的操作
        #     current = current.right
        # return True


        # 递归的方式实现
        # 使用递归对二叉树进行中序遍历，遍历的结果必须有序才符合条件
        # 遍历的每一次操作都需要对比

        def middle(node, res):
            if not node:
                return True
            if res and node.val <= res[-1]: return False
            if node.left: 
                if not middle(node.left, res): return False
                
            if res and node.val <= res[-1]: return False

            res.append(node.val)

            if node.right: 
                if not middle(node.right, res): return False
            return True
        
        res = []
        return middle(root, res)


        # 递归分析
        # 1. append + left
        # 2. append + left
        # x. 最左的所有节点都放在栈中了，拿出栈顶元素（栈顶元素就是树的左叶子节点）,将值放入结果中
        # x + 1. 回溯找到将右边的第一个节点，左同样的1到n的递归

        
# @lc code=end

