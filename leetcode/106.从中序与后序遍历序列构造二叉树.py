#
# @lc app=leetcode.cn id=106 lang=python
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # 解法，从后序遍历中的末尾元素可以找到第一个根结点，找到该节点在中序遍历中的位置
        # 此时该位置前的元素为左孩子，后面的元素为又孩子
        # 递归继续对前后两个孩子进行同样操作

        # 难度： 1. 树的还原 2. 递归返回

        # TODO - recoding
        # 递归函数
        def helper(in_left, in_right):
            # if there is no elements to construct subtrees
            # 4. 第三步中的 index+1 in_right 当到达同一个点时也就是不可再分割是，就是index+1 > in_right，所以返回空
            if in_left > in_right:
                return None
            
            # pick up the last element as a root
            # 1. 从后序遍历中获取根结点，并生成根结点TreeNode
            val = postorder.pop()
            root = TreeNode(val)

            # root splits inorder list
            # into left and right subtrees
            # 2. 在中序遍历中找到根节点的索引值
            index = idx_map[val]
 
            
            # 3. 将根节点左右两边的值进行递归生成新的根节点和子树
            #    因为后续遍历找到根节点是从右边子树开始所以，先对右边左递归
            #    这里传入的参数有两个作用，第一用来限定递归次数也就是分割次数，第二使用来判断是否已经到达叶子节点

            # build right subtree
            root.right = helper(index + 1, in_right)
            # build left subtree
            root.left = helper(in_left, index - 1)
            return root
        # 最终递归结束后返回给第一次调用的根节点
        
        # build a hashmap value -> its index
        # 将list列表转换为哈希表，方便定位元素
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper(0, len(inorder) - 1)

        # 时间复杂度分析：
        # 递归树分析   


        # 时间复杂度：
        # 由主定理考虑： 
        # T(n) = aT(n/b) + f(n) 表示将 T(n) 的问题分解为a个 T(n/b)，
        # 在每次递归中二叉树涉及到的规模为初始问题的两个子问题a=2，因为左右子树在递归中每次各计算一次所以这里b=2, 
        # logb(a) log以b为底的a表示问题被分解为a个子问题规模, O(n**logb(a))
        # f(n)


        # 空间复杂度：O(N)存储整棵树。


        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/5_tree
"""