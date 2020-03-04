#
# @lc app=leetcode.cn id=297 lang=python
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # 对二叉树使用深度优先遍历
    # 二叉树的DFS BFS
    # BFS:
    #         queue_l = []
        # queue_l.append(root)

        # while queue_l:
        #     node = queue_l.pop(0)
        #     if node.right:
        #         queue_l.append(node.right)
        #     if node.left:
        #         queue_l.append(node.left)
        #     if not queue_l:
        #         return node.val

    # 深度遍历
    # 不使用静态变量 使用递归
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def recursive_serializer(node, string):
            if node is None:
                string += "None,"
            else:
                string += str(node.val) + ","
                string = recursive_serializer(node.left, string)
                string = recursive_serializer(node.right, string)
            print string
            return string
        return recursive_serializer(root, '')


    # 反序列化，将数组转化成二叉树
    # 使用了递归实现了序列化，侧同理反序列化也使用递归
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def recursive_serializer(data):
            if data[0] == "None":
                data.pop(0)
                return None
            
            node = TreeNode(data[0])
            data.pop(0)
            node.left = recursive_serializer(data)
            node.right = recursive_serializer(data)
            return node

        return recursive_serializer(data.split(','))

        


        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

