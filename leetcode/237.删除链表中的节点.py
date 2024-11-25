#
# @lc app=leetcode.cn id=237 lang=python
#
# [237] 删除链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        t = node.next
        node.val = t.val
        node.next = t.next
        t = None

        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""