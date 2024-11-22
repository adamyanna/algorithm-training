#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    r = None
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        Solution.r = result

        while True:

            if l1 and l2:
                t_sum = l1.val + l2.val

                l1 = l1.next
                l2 = l2.next
            elif not l1 and l2:
                t_sum = l2.val
                l2 = l2.next
            elif not l2 and l1:
                t_sum = l1.val
                l1 = l1.next
            else:
                t_sum = 0

            Solution.r.next = ListNode(0)

            if Solution.r.val != 0:
                t_sum = t_sum + Solution.r.val

            if t_sum >= 10:
                t_sum = t_sum - 10
                Solution.r.next.val = 1
            else:
                Solution.r.next.val = 0

            Solution.r.val = t_sum



            if not l1 and not l2:
                if Solution.r.next.val == 0:
                    Solution.r.next = None
                break

            Solution.r = Solution.r.next


        print result

        return result


            
        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/4_linked_list
"""