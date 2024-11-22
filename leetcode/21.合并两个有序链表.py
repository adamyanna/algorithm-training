#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # recontect len n m
        # method1 : read all and sort  time- fuckedup
        # method2 : sort insert into long

        # 1. l1 between l2
        # 2. l1 head of l2
        # 3. l1 tail of l2

        # l1 ---------
        # l2    ------

        if not l1 and not l2:
            return None
        elif not l1 and l2:
            return l2
        elif l1 and not l2:
            return l1
        else:
            pass

        if l1.val < l2.val:
            head = l1
            tail = l2
        else:
            head = l2
            tail = l1
        result = head
        while head:
            if not head or not tail:
                break
            if not head.next and tail:
                head.next = tail
                break
            while head.next.val >= tail.val:
                tmp = ListNode(tail.val)
                tmp.next = head.next
                head.next = tmp
                tail = tail.next
                if not tail and head:
                    break
            head = head.next
        return result

            


# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/4_linked_list
"""