#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        l_merge = []
        for l in lists:
            if l:
                l_merge.append((l.val, l))
        if not l_merge:
            return None
        l_merge = sorted(l_merge, key=lambda k: k[0])
        print l_merge
        while len(l_merge) > 1:
            i = 0
            new_l_merge = []
            while i < len(l_merge) / 2:
                new_l = self.mergeTwoLists(l_merge[i][1], l_merge[len(l_merge) - 1 -i][1])
                l_merge.pop(i)
                l_merge.pop(len(l_merge) - 1 -i)
                new_l_merge.append((new_l.val, new_l))
            if l_merge:
                new_l_merge.extend(l_merge)
            l_merge = new_l_merge
        return l_merge[0][1]


    def mergeTwoLists(self, l1, l2):
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

