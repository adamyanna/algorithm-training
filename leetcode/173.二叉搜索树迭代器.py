#
# @lc app=leetcode.cn id=173 lang=python
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    # 首先根据题意，要实现的是一个每次取出最小数的操作，所以，对于一个二叉搜索树，只需要进行中序遍历即可得到一个排序序列
    # 但是要求空间复杂度只能小于等于这个树的高度，且取出和查看都是O(1)
    # 1. 对于此要求，第一对树只进行中序的遍历的左边，并将值存入一个栈中
    # 2. 每次取出的时候需要对pop出来节点，查看其是否存在右子树，如果存在则将其右子树进行递归，找到下一个最小值
    # 3. 递归的过程中，将找到的值push入栈
    # 时间复杂度上 next操作的平均时间复杂度近似为1，最差时间复杂度依然为N

    def __init__(self, root):
        
        # Stack for the recursion simulation
        self.stack = []
        
        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)
        
    def _leftmost_inorder(self, root):
        
        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        """
        
        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()
        
        # Need to maintain the invariant. If the node has a right child, call the 
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

