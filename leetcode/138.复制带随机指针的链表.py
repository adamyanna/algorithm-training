#
# @lc app=leetcode.cn id=138 lang=python
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # 用来保存当前访问的节点深拷贝出来的新节点
        self.hash_map = {}

        def recursive_copy(head_node):
            if not head_node:
                return None

            # 1. hash_map 中保存了当前访问节点和初始化的拷贝节点
            # 如果不存在则证明该节点还没创建
            new_node = self.hash_map.get(head_node)
            if not new_node: 
                # 1. 拷贝值创建新节点， 并存入hash_map
                new_node = Node(head_node.val, None, None)
                self.hash_map.update({head_node: new_node})
            else:
                # 2. 在已经拷贝过的node里找到了已经新建的node就要直接返回，否则会导致循环递归，最终达到递归上限
                return new_node

            # 3. 拷贝自己的next，如果存在直接返回
            new_node.next = recursive_copy(head_node.next)
            # 4. 拷贝自己的random，如果存在直接返回
            new_node.random = recursive_copy(head_node.random)

            return new_node

        return recursive_copy(head)




        
# @lc code=end

