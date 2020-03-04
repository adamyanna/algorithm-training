#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 两个指针，一个一次两步，一个一次一步，如果出现
        # 环，则回出现快指针会第二次超过慢指针的情况

        if not head or not head.next:
            return False

        p1 = head
        p2 = head.next
        while p1 != p2:
            if not p1 or not p2 or not p2.next:
                return False
            p1 = p1.next
            p2 = p2.next.next

        return True



        
# @lc code=end

