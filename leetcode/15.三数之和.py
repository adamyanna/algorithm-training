#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Anylize
        # 1. use set
        # 2. minimize the time
        # result = set()
        # result_dict = {}
        # for a in nums:
        #     result_dict.update({[a]: a})
        # for b in nums:
        #     for i in result_dict.iterkeys():
        #         result_dict[i] += b
        #         i.append(b)
        # for c in nums:
        #     for i in result_dict.iterkeys():
        #         result_dict[i] += c
        #         i.append(c)
        # print result_dict
        # for k, v in result_dict.iteritems():
        #     if v == 0:
        #         result.add(tuple(k))

        # return result


        # sort and 2 points

        result = []
        nums.sort() #nlog(n)
        k = 0
        while nums and len(nums) > 2 and nums[k] <= 0 and k < len(nums) -1: # n
            if nums[k] > 0: break # 最外层循环只遍历小于等于0的值，如果遇到大于0的值直接跳出
            # 
            # 遇到重复直接前移一个元素，去除重复答案
            if k != 0 and nums[k] == nums[k-1]: k+=1; continue 
            i = k + 1
            j = len(nums) -1
            # 循环n次
            while i < j:
                s = nums[i] + nums[k] + nums[j]
                if s < 0:
                    i += 1
                    while i <j and nums[i] == nums[i - 1]: i += 1 # 去重
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1 # 去重
                else:
                    t = [nums[i], nums[k], nums[j]]
                    result.append(t)
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
            k += 1

        return result


    # T: nlog(n) + n**2  == n**2
        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/2_2pointers
"""