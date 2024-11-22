#
# @lc app=leetcode.cn id=443 lang=python
#
# [443] 压缩字符串
#

# @lc code=start
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # 实现空间复杂度为1的原地算法
        # 在python中使用切片无法实现原地算法，原地算法需要对原数组中的值进行修改，例如直接替换、pop、insert

        # count, j, i = 1, 0, 0
        # while i < len(chars) - 1:
        #     i += 1
        #     if chars[i] == chars[i - 1]:
        #         count += 1
        #         if j == 0: j = i
        #         if i == len(chars) - 1 and count > 1:
        #             count_l = str(count).split(",")
        #             chars = chars[0:j] + count_l
        #     else:
        #         if count > 1:
        #             count_l = str(count).split(",")
        #             chars = chars[0:j] + count_l + chars[i:]
        #             j = 0
        #             count = 1
        #             i = i - (i - j) + len(count_l)
        # print chars
        # return len(chars)

        # 实现空间复杂度为1的原地算法
        count, i = 1, 0
        while i < len(chars) - 1:
            i += 1
            if chars[i] == chars[i - 1]:
                chars.pop(i)
                i -= 1
                count += 1
                if i == len(chars) - 1 and count > 1:
                    chars.extend(list(str(count)))
                    break
            else:
                if count > 1:
                    count_l = list(str(count))
                    for v in count_l:
                        chars.insert(i, v)
                        i += 1
                    count = 1
        return len(chars)
        # 空间复杂度O(1) 使用3个常量存储
        # 时间复杂度O(N)

        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""