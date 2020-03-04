#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 
        if not nums: return 0
        if len(nums) == 1: return 1
        i , c = 0, 0
        while i < len(nums) - 1:
            i += 1
            if nums[i] != nums[c]:
                if nums[c] == nums[c -1]:
                    nums[c:i + 1] = [nums[i] for _ in range(c, i + 1)]
                c += 1
            else:
                if nums[c] != nums[c -1]:
                    c = i
        if c == len(nums) - 1 and nums[c -1] != nums[len(nums) - 1]:
            return len(nums)
        if c == 0:
            return 1
        return c


        # Double pointer

        # @Time complexity: O(n)
        # @Space complexity: O(1)


# @lc code=end

