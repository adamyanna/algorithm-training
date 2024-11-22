#
# @lc app=leetcode.cn id=445 lang=python
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """

    # TODO
    # Mark - this is a python 3 implementation
    # finish python2 version and rewrite with stack push pop
    def addTwoNumbers(self, l1, l2):
        def add(num1, num2, i, j):
            if not i or not j:
                return 0
            # nums1为长串，在长串本身上进行修改，temp值为该点值加进位值，递归调用i.next
            if num1 > num2:
                temp = i.val + add(num1 - 1, num2, i.next, j)
            else:
            # 递归调用直到两个长度相等，继续递归相同长度的两个链表，
            # 当i next和j next到达末尾时，第一次返回，相加并修改i的值为tmp%10，返回进位值1或者0
            # 前一个相加会继续更新，直到返回到num1》num2的位置
                temp = i.val + j.val + add(num1, num2, i.next, j.next)
            i.val = temp % 10
            return temp // 10

        num1 = num2 = 0
        cur = l2
        while cur:
            num2 += 1
            cur = cur.next
        cur = l1
        while cur:
            num1 += 1
            cur = cur.next
        
        if num2 > num1:
            l1, l2 = l2, l1
            num2, num1 = num1, num2

        if add(num1,num2,l1, l2):
            l2 = ListNode(1)
            l2.next = l1
            l1 = l2
        return l1

# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""