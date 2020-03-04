#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        p = 0
        if nums1:
            for n2 in nums2:
                n = p
                m = len(nums1) - 1
                while True:
                    i = int((m - n) / 2) + n
                    if n == m:
                        if n2 > nums1[n]:
                            p = n + 1
                            break
                        else:
                            p = n
                            break
                    if n == m - 1:
                        if nums1[n] <= n2 <= nums1[m]:
                            p = n + 1
                            break
                        elif n2 < nums1[n]:
                            p = n
                            break
                        elif n2 > nums1[m]:
                            p = m + 1
                            break
                        else:
                            break
                    if n2 == nums1[i]:
                        p = i
                        break
                    elif n2 < nums1[i]:
                        m = i
                    else:
                        n = i
                nums1.insert(p, n2)
        else:
            nums1 = nums2
        if len(nums1) % 2 > 0:
            return nums1[int(len(nums1) - 1) / 2]
        else:
            return float((nums1[int(len(nums1) /2)] + (nums1[int(len(nums1) /2 - 1)])) / 2.0)

    # TODO need to do another alternative
                
# @lc code=end

