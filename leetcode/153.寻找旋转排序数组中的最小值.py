#
# @lc app=leetcode.cn id=153 lang=python
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]

        return nums[0]

        # 将时间复杂度降低到 logn
        # 做法是对数组进行二分搜索
        # 每次搜索只保留之后，将中间点和数组第一个元素比较大小
        # 如果大，那就是最小值在右侧，如果小则在左侧
        # 直到找到第一个小于其前值的元素
        # 因为翻转后的最小值一定在二分查找分出来的两个序列中
        # 时间复杂度可以从n降低到logn


# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/1_array_hashing
"""