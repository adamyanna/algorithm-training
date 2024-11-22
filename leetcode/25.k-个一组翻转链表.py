#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if k == 0:
            return head
        if head == None or head.next == None:
            return head
        stack = []
        first = None
        last = None
        while True:
            if not head and len(stack) < k:
                if not first:
                    return stack[0]
                last.next = stack[0]
                return first
            if len(stack) == k:
                i = k - 1
                while i > 0:
                    stack[i].next = stack[i - 1]
                    if i -1 == 0: stack[i -1].next = None
                    i -= 1
                if not last and not first:
                    first = stack[k - 1]
                else:
                    last.next = stack[k - 1]
                last = stack[0]
                stack = []
            if not head and not stack:
                return first
            stack.append(head)
            head = head.next


# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/4_linked_list
"""