#
# @lc app=leetcode.cn id=151 lang=python
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # python
        # 解法1: 先用strip，然后split，然后反向读取list在转为字符串
        # 解法2: 不使用额外n空间，先strip，然后在字符串前加两个空格，然后读取到第一个单词，
        # 将开始坐标和单词结束坐标的字符加到字符串末尾并删除，依次对所有单词做同样操作，直到找到末尾坐标（后面出现两个连续空格）
        # 解法3：不使用额外n空间，原地算法，双指针


# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/1_array_hashing
"""