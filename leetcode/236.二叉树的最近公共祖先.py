#
# @lc app=leetcode.cn id=236 lang=python
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # BFS - Breadth first search    while loop
        # DFS - depth first search      recursive

        # recursive tree
        #       a
        #    b      z
        #  c   f
        # d  e

        stack = []
        find = []

        # 返回根结点
        if root == q or root == p:
            return root

        def depth_search(node, p, q):

            if node.val == p.val or node.val == q.val:
                # 找到第二个元素返回True，这时候整个递归都会返回，并且不再修改结果
                if find:
                    return True
                # 找到第一个元素后在find数组中标记
                # 并且将第一个找到的元素也考虑在可能的答案根结点上
                find.append(True)
                stack.append(node)
            
            # 考虑末尾节点，当节点为叶子节点时，直接对该节点返回False
            # 如果当前匹配第一次的节点就是叶子节点，需要将该节点移除缓存栈
            if node.left == None and node.right == None:
                if stack[-1] == node: stack.pop(-1)
                return False

            # 没有匹配的情况下，需要将每个非叶子节点加入缓存栈
            if not find: stack.append(node)

            # 对左右子树递归
            if node.left:
                if depth_search(node.left, p, q): return True
            if node.right:
                if depth_search(node.right, p ,q): return True

            # 如果没有一次匹配则回溯到本节点后从缓存栈移除
            # 如果当前节点就是缓存栈顶部节点，则移除，因为上面的左右子树递归没有找到第二个匹配项
            if not find or stack[-1] == node: stack.pop(-1)

        depth_search(root, p, q)
        return stack[-1]




        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""