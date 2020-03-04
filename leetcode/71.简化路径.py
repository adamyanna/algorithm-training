#
# @lc app=leetcode.cn id=71 lang=python
#
# [71] 简化路径
#

# @lc code=start
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # ❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌
        # path = list(path)
        # slash = [0] if path[0] == "/" else []
        # i = 0
        # while i < len(path):
        #     # 遇到//不处理
        #     i += 1
        #     if not (i +1 < len(path)): break
        #     if (path[i] == path[i-1] == "/"):
        #         path.pop(i)
        #         i -= 1
        #         continue
        #     elif path[i] == "/" and path[i-1] != "/":
        #         slash.append(i)
        #         continue
        #     if path[i] == "." and path[i + 1] == ".":
        #         if i + 2 < len(path):
        #             if len(slash) < 2:
        #                 path = path[i + 2:]
        #                 i = 0
        #             else:
        #                 path = path[:slash[-2]] + path[i + 2:]
        #                 i = slash[-2]
        #             slash.pop(-1)
        #         elif i + 2 == len(path):
        #             if len(slash) < 2:
        #                 path = path[:i]
        #             else:
        #                 path = path[:slash[-2]] + path[i + 2:]
        #     elif path[i] == "." and path[i + 1] != ".":
        #         path.pop(i)
        #         path.pop(i)
        #         i -= 1
        # while path[-1] == ".": path.pop(-1)
        # while len(path) > 1 and path[-1] == "/": path.pop(-1)
        # return "".join(path)
        # ❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌TRASH

        #解决方案： 栈  split("/")
        # 遇到这样的字符过滤的问题，一定要想到栈
                    
        stack = []
        l = path.split("/")
        for v in l:
            # case
            if not v:
                pass
            elif v == ".":
                pass
            elif v == '..':
                if stack: stack.pop(-1)
            else:
                stack.append(v)
        return "/" + "/".join(stack)
                

                
                


        
# @lc code=end

