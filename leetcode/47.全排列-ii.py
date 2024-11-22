#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # def do_swap(l, start, end):
        #     for i in range(start, end):
        #         if l[end] == l[i]:
        #             return False
        #     return True


        # def backtrack(start=0):
        #     if start == n:
        #         result.append(nums[:])
            
        #     for i in range(start, n):
        #         # if i > 0 and nums[i] == nums[i - 1] and pre[i] == 0:
        #         #     continue
        #         if do_swap(nums, start, i):
        #             nums[i], nums[start] = nums[start], nums[i]
        #             backtrack(start + 1)
        #             nums[i], nums[start] = nums[start], nums[i]

        # nums.sort()
        # n = len(nums)
        # result = []
        # backtrack()
        # return result

        def backtrack(first=0):
            if first == n:
                result.append(nums[:])
            s = set()
            for i in range(first, n):
                if nums[i] in s: continue
                s.add(nums[i])
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

            
        n = len(nums)
        result = []
        backtrack()
        return result


    
        # def backtrack(start=0):
        #     if start == n:
        #         # if nums not in result:
        #         result.append(nums[:])
        #     for i in range(start, n):
        #         if i + 1 < n and nums[i] == nums[i + 1]:
        #             continue
        #         if i==start and pre.get(i) and nums[:start] in pre.get(i):
        #             continue
        #         nums[i], nums[start] = nums[start], nums[i]
        #         if start ==i:
        #             if not pre.get(i):
        #                 pre[i] = [nums[:start]]
        #             else:
        #                 pre[i].append(nums[:start])
        #         backtrack(start + 1)
        #         nums[i], nums[start] = nums[start], nums[i]

        # pre = {}
        # n = len(nums)
        # result = []
        # backtrack()
        # return result


    # Python 3 time complexity great
    # class Solution:
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     self.res = []
    #     check = [0 for i in range(len(nums))]
        
    #     self.backtrack([], nums, check)
    #     return self.res
        
    # def backtrack(self, sol, nums, check):
    #     if len(sol) == len(nums):
    #         self.res.append(sol)
    #         return
        
    #     for i in range(len(nums)):
    #         if check[i] == 1:
    #             continue
    #         if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
    #             continue
    #         check[i] = 1
    #         self.backtrack(sol+[nums[i]], nums, check)
    #         check[i] = 0

    # def permuteUnique(self, nums):
    #     nums.sort()
    #     self.res = []
    #     check = [0 for _ in range(len(nums))]

    #     self.backtrack([], nums, check)
    #     return self.res

    # def backtrack(self, sol, nums, check):
    #     if len(sol) == len(nums):
    #         self.res.append(sol)
    #         return

    #     for i in range(len(nums)):
    #         if check[i] == 1:
    ##             continue
    #         if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
    #             continue
    #         check[i] = 1
    #         self.backtrack(sol + [nums[i]], nums, check)
    #         check[i] = 0

                    
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/5_back_tracking
"""