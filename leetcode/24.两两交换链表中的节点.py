#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # recursive
        #  1 -> 2 -> 3
        #  第一步暂存1.next 也就是2
        #  第二步更新1的next为2的next，这里就是次操作的递归
        #  第三部更新暂存的2的next为1

        # 思考： 先换第一个和第二个，然后在思考后面怎么换
        if head == None or head.next == None:
            return head
        read_p = ListNode(0)
        read_p = head.next
        head.next = self.swapPairs(read_p.next)
        read_p.next = head
        return read_p
            

# @lc code=end

