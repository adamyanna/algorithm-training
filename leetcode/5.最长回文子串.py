#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # A: find the same from start to end as start of iterable
        result = {}

        for i in range(len(s)):

            r = ""
            k = 0
            j = 0
            if i + 1 >= len(s):
                continue
            if s[i] == s[i+1]:
                j = i
                k = i + 1
                while j >= 0 and k < len(s) and s[j] == s[k]:
                    r = s[j] + r
                    r += s[k]
                    j -= 1
                    k += 1
            if r:
                result.update({len(r): r})
            if i - 1 >= 0 and i + 1 < len(s) and s[i-1] == s[i+1]:
                r = s[i]
                j = i - 1
                k = i + 1
                while j >= 0 and k < len(s) and s[j] == s[k]:
                    r = s[j] + r
                    r += s[k]
                    j -= 1
                    k += 1
            if r:
                result.update({len(r): r})
        print result
        if result:
            return result[max(result.keys())]
        elif s:
            return s[0]
        else:
            return ""





        # last_i = len(s) -1
        # result = ""
        # for i in range(len(s)):
        #     if s[i] == s[last_i]
        #         last_i = last_i - 1
        #         result += s[i]
        #     else:
        #         if s[i + 1] == s[last_i]:
        #             continue
        #         elif s[i] == s[last_i -1]:
        #             last_i = last_i -1
        #         else:
        #             last_i = last_i -1

        # reutrn result


        
# @lc code=end

