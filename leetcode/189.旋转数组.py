#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 旋转数组
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # l = len(nums)
        # n = 1
        # cache = nums[0]
        # cur = n*k
        # while cur != 0:
        #     cur = n*k
        #     if n*k / l > 0:
        #         cur = cur % l
        #     tmp = nums[cur]
        #     nums[cur] = cache
        #     cache = tmp
        #     n += 1
        #     if cur == 0 and n < l:
        #         cur += 1

        l = len(nums)
        n = 0
        cache = nums[0]
        cur = k
        start_p = 0
        # update = l / k if l % k == 0 else 0
        update_cur = False
        while n < l:
            if n > 0 and cur == start_p and not update_cur:
                cur = cur + 1
                cache = nums[cur]
                start_p = cur
                update_cur = True
                continue

            # if update != 0 and n > 0 and n % update == 0 and not update_cur:
            #     cur = cur + 1
            #     cache = nums[cur]
            #     update_cur = True
            #     continue
            cur = cur if n == 0 else cur + k
            update_cur = False
            if cur / l > 0:
                cur = cur % l
            tmp = nums[cur]
            nums[cur] = cache
            cache = tmp
            n += 1
        print nums

# @lc code=end

