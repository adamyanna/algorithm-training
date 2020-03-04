#
# @lc app=leetcode.cn id=75 lang=python
#
# [75] 颜色分类
#

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # 因为是线性数组，一次遍历使用双指针最为高效
        # 因为该题目为三中类型的元素
        # 所以需要双指针来跟踪边缘
        # 增加一个循环指针

        # p = 0
        # edge_l = 0
        # edge_r = len(nums) - 1
        # while p <= edge_r:
        #     if nums[p] == 0:
        #         #左边缘右移
        #         nums[p], nums[edge_l] = nums[edge_l], nums[p]
        #         edge_l += 1
        #         p += 1
        #     elif nums[p] == 2:
        #         #和右边缘护环
        #         nums[p], nums[edge_r] = nums[edge_r], nums[p]
        #         edge_r -= 1
        #     elif nums[p] == 1:
        #         p += 1

        # return nums


        # 暴力

        # i = 0
        # j = len(nums) - 1
        # while i <= j:
        #     if nums[i] = 

        if (1 not in nums and 2 not in nums) or (1 not in nums and 0 not in nums) or (0 not in nums and 2 not in nums):
            return nums
    
        i = 0
        count = 0
        while i < len(nums) and len(nums) > 1:
            if nums[i] == 0:
                nums.insert(0, 0)
                nums.pop(i + 1)
                i += 1
                if count: count = 0
            elif nums[i] == 2:
                if count >= len(nums) - i:
                    break
                nums.append(2)
                nums.pop(i)
                count += 1
            else:
                i += 1
                if count: count = 0

        return nums




        
# @lc code=end

