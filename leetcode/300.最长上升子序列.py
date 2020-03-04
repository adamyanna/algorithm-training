#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #  DP + BS
        # dynamic programming + binary search
        dp = []
        for v in nums:
            if not dp or v >  dp[-1]:
                dp.append(v)
                continue
            i, j = 0, len(dp)
            # 二分查找找到第一个最大的，也就是大小最接近v而且大于v的数
            while i < j:
                m = (i + j) // 2  # // 表示对商向下取整
                if dp[m] < v: i = m + 1
                else: j = m
            #既保留前者状态又更新最新状态的替换
            dp[i] = v
        return len(dp)

#         # Dynamic programming + Dichotomy.
# class Solution:
#     def lengthOfLIS(self, nums: [int]) -> int:
#         tails, res = [0] * len(nums), 0
#         for num in nums:
#             i, j = 0, res
#             while i < j:
#                 m = (i + j) // 2
#                 if tails[m] < num: i = m + 1 # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
#                 else: j = m
#             tails[i] = num
#             if j == res: res += 1
#         return res

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
# @lc code=end

