#
# @lc app=leetcode.cn id=204 lang=python
#
# [204] 计数质数
#

# @lc code=start
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # prime number
        # 从2和3开始，每次加1，并对现在已经保存的素数取模也就是取余数，直到n


        # 欧拉晒法

        # brute force
        # prime_list = []
        # for i in range(2, n):
        #     if not prime_list:
        #         prime_list.append(i)
        #     else:
        #         is_prime = True
        #         j = 0
        #         while prime_list[j] <= i/prime_list[j]:                
        #             if i % prime_list[j] == 0:
        #                 is_prime = False
        #                 break
        #             j += 1
        #         if is_prime: prime_list.append(i)


        # return len(prime_list)


        # 埃式筛法
        # if n < 2: return 0
        # visited = [False]*n
        # ans = n - 2

        # i = 2
        # while i <= n/i:
        #     if not visited[i]:
        #         j = i * i
        #         while j < n:
        #             if not visited[j]: ans -= 1
        #             visited[j] = True
        #             j += i
        #     i += 1

        # return ans






        # todo 了解欧拉筛法
        prime = [0 for i in range(n)]  # 全部初始化为0
        common = [] # 存放素数
        for i in range(2, n): # 开筛
            if prime[i] == 0:
                common.append(i)
            for j in common:
                if i * j > n - 1:
                    break
                prime[i * j] = 1
                if i % j == 0:
                    break
        return len(common)






# @lc code=end

