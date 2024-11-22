#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        # 解法： 假设相交前A的长度为L1，相交前B的长度为L2，相交长度为L3
        # 则总有 L1 + L3 + L2 = L2 + L3 + L1
        # 所以，得出结论双指针遍历A，B，当其中任何一个指针到链表末尾时，将指针指向另一个链表
        # 只需要交换一次，即可找到相等的点
        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""