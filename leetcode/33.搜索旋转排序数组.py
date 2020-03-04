#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # time complexity logN  

        # length = len(nums)
        # if target > nums[0]:
        #     i, j = 0, length / 4
        #     while j < length:
        #         if target == nums[j]:
        #             return j
        #         elif target < nums[j]:
        #             if j == i + 1 or i == j + 1:
        #                 return -1
        #             i = j
        #             j = j / 2                       
        #         else:
        #             if j == i + 1 or i == j + 1:
        #                 return -1
        #             i = j
        #             j = (length - 1 - j) / 2 + j
        # elif target < nums[length - 1]:
        #     i, j = 0, 3* length / 4
        #     while j < length:
        #         if target == nums[j]:
        #             return j
        #         elif target < nums[j]:
        #             if j == i + 1 or i == j + 1:
        #                 return -1
        #             i = j
        #             j = j / 2                       
        #         else:
        #             if j == i + 1 or i == j + 1:
        #                 return -1
        #             i = j
        #             j = (length - 1 - j) / 2 + j

        # elif target == nums[length - 1]:
        #     return length - 1
        # elif target == nums[0]:
        #     return 0
        # else:
        #     return -1


        length = len(nums)
        if not nums:
            return -1
        elif target == nums[length - 1]:
            return length - 1
        elif target == nums[0]:
            return 0
        elif nums[length - 1] < nums[0] and nums[length - 1] < target < nums[0]:
            return -1
        else:
            pass

        i, j = 0, length -1
        while i <= j:
            m = i + (j - i) / 2

            mt= target
            mV= "M %s" % nums[m]
            mI= "I %s" % nums[i]
            mJ= "J %s" % nums[j]

            if target == nums[m]:
                return m
            elif target == nums[i]:
                return i
            elif target == nums[j]:
                return j
            elif i == j:
                return -1

            if nums[length - 1] > nums[0]:
                # not rotated
                if target < nums[m]:
                    j = m -1
                else:
                    i = m + 1
            else:
                # rotated
                if nums[m] > nums[length -1]:
                    # middle in the left side
                    if target < nums[m] and target < nums[0]:
                        i = m + 1
                    elif target < nums[m] and target > nums[0]:
                        j = m - 1
                    elif target > nums[m]:
                        i = m + 1
                    else:
                        return -1
                elif nums[m] < nums[length -1]:
                    # middle in the right side
                    # or nums are not rotated
                    if target < nums[m]:
                        j = m - 1
                    elif target > nums[m] and target > nums[0]:
                        j = m - 1
                    elif target > nums[m] and target < nums[0]:
                        i = m + 1
                    else:
                        return -1

        return -1
            








# @lc code=end

