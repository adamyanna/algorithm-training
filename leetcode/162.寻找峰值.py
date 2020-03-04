#
# @lc app=leetcode.cn id=162 lang=python
#
# [162] 寻找峰值
#

# @lc code=start
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 使用迭代的二分查找或者递归的二分搜索的方法

        # 解法： 1. 递归
        # 找出二分搜索的中间点
        # 比较是否 中间点的值大于其后一个值，如果大于则证明，中间点位于一个局部下降的位置，
        # 那么它左边肯定有至少一个peek点，那么继续对左边做二分搜索
        # 如果，中间点的值小于其后面一个值，那么中间点在一个局部上升位置
        # 那么它右边肯定有一个peek，递归
        # 最终l r相等就可以得到结果

        #public class Solution {
        #     public int findPeakElement(int[] nums) {
        #         return search(nums, 0, nums.length - 1);
        #     }
        #     public int search(int[] nums, int l, int r) {
        #         if (l == r)
        #             return l;
        #         int mid = (l + r) / 2;
        #         if (nums[mid] > nums[mid + 1])
        #             return search(nums, l, mid);
        #         return search(nums, mid + 1, r);
        #     }
        # }


        def search_peek(nums, l, r):
            if l == r:
                return l

            middle = (l + r) /2
            # \  down from middle to middle + 1
            if nums[middle] > nums[middle + 1]:
                return search_peek(nums, l, middle)
            # / up from middle to middel +1
            else:
                return search_peek(nums, middle + 1, r)


        return search_peek(nums, 0, len(nums) -1)



# @lc code=end

