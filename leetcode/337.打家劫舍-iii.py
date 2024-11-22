#
# @lc app=leetcode.cn id=337 lang=python
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # * 返回一个大小为 2 的数组 arr
        # arr[0] 表示不抢 root 的话，得到的最大钱数
        # arr[1] 表示抢 root 的话，得到的最大钱数 */
        # int[] dp(TreeNode root) {
        #     if (root == null)
        #         return new int[]{0, 0};
        #     int[] left = dp(root.left);
        #     int[] right = dp(root.right);
        #     // 抢，下家就不能抢了
        #     int rob = root.val + left[0] + right[0];
        #     // 不抢，下家可抢可不抢，取决于收益大小
        #     int not_rob = Math.max(left[0], left[1])
        #                 + Math.max(right[0], right[1]);
            
        #     return new int[]{not_rob, rob};
        # }

        # 对于二叉树，满足条件的情况下，必须每次抢劫都隔一层
        #     0
        #    1 1
        #  1 0 0 0
        # 0 0           0都是可以抢的
        # 所以抢了根节点就不能再抢他的字节点
        # 深度遍历，从左下开始，求每个根节点要抢和不抢的大小
        # dp: [not_r, r]
        # dp[r] = ndoe.val + dp_sub_l[0] + dp_sub_r[0]  必须是其和其子节点不抢的和，抢了自己就不能在抢自己节点
        # dp[not_r] = max(dp_sub_l[1],dp_sub_l[0]) + max(dp_sub_r[1],dp_sub_r[0]) 如果该点不抢的话，
        # 它自己的字节点可以抢也可以不抢，抢不抢它的左节点取决于，抢的利润和不抢的利润，所以这里右边也一样

        def dp_recursive(node):
            if not node:
                return [0,0]
            dp_sub_l = dp_recursive(node.left)
            dp_sub_r = dp_recursive(node.right)
            dp_r = node.val + dp_sub_l[0] + dp_sub_r[0]
            dp_not_r = max(dp_sub_l[1],dp_sub_l[0]) + max(dp_sub_r[1],dp_sub_r[0])
            return [dp_not_r, dp_r]

        return max(dp_recursive(root))

        


# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""