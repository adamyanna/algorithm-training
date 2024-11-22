#
# @lc app=leetcode.cn id=215 lang=python
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # 第k个最大元素，第一次尝试
        # 分析，找到排序后的第k个最大元素，就是找到排序后从尾部数到k个元素
        # 如果直接排序的话需要时间复杂到到nlogn
        # 其实就是一次快排，最终达成的目的就是在序列的n-k的位置，
        # 其左边的数全都比他小，右边的数全都比他大
        # 利用快速排序的特性，这时候只需要在,将k-n定位在左右两边的一边
        # 这种情况下每次只需要对快排的一边进行操作，
        # 可以将时间复杂度降低到 N


        # 时间复杂度[edit]
        # 与快速排序类似，快速选择算法在平均状况下有着不错的表现，
        # 但是对于基准值的选择十分敏感。如果基准值选择上佳，搜索范围每次能够指数级减少，
        # 这样一来所耗时间是线性的(即O(n))。但如果基准值选择非常不好，
        # 使得每次只能将搜索范围减少一个元素，则最糟的总体时间复杂度是平方级的(O(n2))：
        # 例如对一个升序排列的数组搜索其最大值，而每次都选择第一个元素作为基准值。


        # 快速选择
        # 快速选择算法的动画演示：选择第22小的元素。
        # 快速选择算法的动画演示：选择第22小的元素。（注意：这和条目中的算法不完全相同）
        # 分类	选择算法
        # 数据结构	数组
        # 最坏时间复杂度	О(n2)
        # 最优时间复杂度	О(n)
        # 平均时间复杂度	O(n)
        # 最坏空间复杂度	O(1)
        # 在计算机科学中，快速选择（英語：Quickselect）是一种从无序列表找到第k小元素的选择算法。它从原理上来说与快速排序有关。与快速排序一样都由托尼·霍尔提出的，因而也被称为霍尔选择算法。[1] 同样地，它在实际应用是一种高效的算法，具有很好的平均时间复杂度，然而最坏时间复杂度则不理想。快速选择及其变种是实际应用中最常使用的高效选择算法。
        # 快速选择的总体思路与快速排序一致，选择一个元素作为基准来对元素进行分区，将小于和大于基准的元素分在基准左边和右边的两个区域。不同的是，快速选择并不递归访问双边，而是只递归进入一边的元素中继续寻找。这降低了平均时间复杂度，从O(n log n)至O(n)，不过最坏情况仍然是O(n2)。
        # 与快速排序一样，快速选择一般是以原地算法的方式实现，除了选出第k小的元素，数据也得到了部分地排序。

        # l = len(nums)
        # base = nums[l-k]
        # i = 0
        # j = l - 1
        # while i < j:
        #     if l - k > l/2:
        #         if nums[i] > 

        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest 
        return select(0, len(nums) - 1, len(nums) - k)



# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/1_array_hashing
"""