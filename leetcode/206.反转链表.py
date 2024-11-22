#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 指针操作，需要留意暂存next和更新last已经current

        last = None
        current = head
        while current:
            tmp_save_next = current.next
            current.next = last
            last = current
            current = tmp_save_next

        return last


# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/4_linked_list
"""