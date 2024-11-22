#
# @lc app=leetcode.cn id=567 lang=python
#
# [567] 字符串的排列
#

# @lc code=start
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 解法1: 复杂窗口匹配法
        # 1. 在s1中找到所有字符的数量
        """
        char_map = {}
        for v in s1:
            if v not in char_map.iterkeys():
                char_map.update({v: 1})
            else:
                char_map.update({v: char_map[v] + 1})
        # 2. 通过滑动窗口匹配s1中的元素数量
        w_l= len(s1)
        i = 0
        max_l = []
        less_l = []
        while i < len(s2) - w_l + 1:
            if max_l and max_l[1] > 0:
                if s2[i+w_l-1] != max_l[0] and s2[i-1] == max_l[0]:
                    max_l[1] -= 1
                elif s2[i+w_l-1] == max_l[0] and s2[i-1] != max_l[0]:
                    max_l[1] += 1
                if max_l[1] > 0:
                    i += 1
                continue
            if less_l and less_l[1] > 0:
                if s2[i+w_l-1] == less_l[0] and s2[i-1] != less_l[0]:
                    less_l[1] -= 1
                elif s2[i+w_l-1] != less_l[0] and s2[i-1] == less_l[0]:
                    less_l[1] += 1
                if less_l[1] > 0:
                    i += 1
                continue
            tmp_count = {}
            j = i
            while j < w_l + i:
                if s2[j] not in char_map.iterkeys():
                    i = j
                    break

                if s2[j] not in tmp_count.iterkeys():
                    tmp_count.update({s2[j]: 1})
                else:
                    tmp_count.update({s2[j]: tmp_count[s2[j]] + 1})
                
                # # 窗口中元素过多
                v = s2[j]
                if tmp_count[v] > char_map[v]:
                    max_l = [v, tmp_count[v] - char_map[v]]
                    break
            
                # 窗口中元素过少(窗口中已经存在的元素数量与s中元素数量的差值大于了当前窗口的剩余长度)
                if char_map[v] - tmp_count[v] > w_l + i - j:
                    less_l = [v, char_map[v] - tmp_count[v] - (w_l + i - j)]
                j += 1
            i += 1
            if tmp_count == char_map:
                return True

        return False
        """
        
        # 解法2: 窗口前后元素更新比对法

        # 1. 在s1中找到所有字符的数量
        char_map = {}
        for v in s1:
            if v not in char_map.iterkeys():
                char_map.update({v: 1})
            else:
                char_map.update({v: char_map[v] + 1})

        window_size = len(s1)
        window_map = {}
        window_left = 0
        window_right = 0

        while window_right < len(s2):

            if s2[window_right] not in char_map.iterkeys():
                window_map = {}
                window_left = window_right + 1
                window_right = window_right + 1
                continue

            if s2[window_right] not in window_map.iterkeys():
                window_map.update({s2[window_right]: 1})
            else:
                window_map.update({s2[window_right]: window_map[s2[window_right]] + 1})

            window_right += 1

            if window_right - window_left > window_size:
                window_map[s2[window_left]] -= 1
                if window_map[s2[window_left]] == 0:
                    window_map.pop(s2[window_left])
                window_left += 1
            if window_map == char_map: return True
        return False



# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""