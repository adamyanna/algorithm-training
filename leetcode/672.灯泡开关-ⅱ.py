#
# @lc app=leetcode.cn id=672 lang=python
#
# [672] 灯泡开关 Ⅱ
#

# @lc code=start
class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        n = min(n, 3)
        if m == 0: return 1
        if m == 1: return [2, 3, 4][n-1]
        if m == 2: return [2, 4, 7][n-1]
        return [2, 4, 8][n-1]

        # lights = [1 for i in range(n)]
        # result = []

        # p = []

        # for m1 in range(m + 1):
        #     m234 = m - m1
        #     for m2 in range(m234 +1):
        #         m34 = m234 - m2
        #         for m3 in range(m34 +1):
        #             m4 = m34 - m3
        #             if m1 % 2 > 0:
        #                 lights = [0 for i in range(n)]
        #             if m2 % 2 > 0:
        #                 for i in range(0, n):
        #                     if (i+1) % 2 == 0:
        #                         if lights[i] == 0:
        #                             lights[i] = 1
        #                         else:
        #                             lights[i] = 0
        #             if m3 % 2 > 0:
        #                 for i in range(0, n):
        #                     if (i + 1) % 2 == 1:
        #                         if lights[i] == 0:
        #                             lights[i] = 1
        #                         else:
        #                             lights[i] = 0
        #             if m4 % 2 > 0:
        #                 if n == 0:
        #                     continue
        #                 elif n in [1, 2, 3]:
        #                     if lights[0] == 0:
        #                         lights[0] = 1
        #                     else:
        #                         lights[0] = 0
        #                 else:
        #                     for k in range(int((n - 1)/ 3) + 1):
        #                         if lights[3 *k] == 0:
        #                             lights[3 * k] = 1
        #                         else:
        #                             lights[3 * k] = 0
        #             r_l = ",".join([str(a) for a in lights])
        #             print m1, m2, m3, m4
        #             p.append([m1, m2, m3, m4])
        #             print "LIGHTS: %s" % lights
        #             result.append(r_l)
        #             lights = [1 for i in range(n)]

        # print len(result)
        # result = set(result)
        # print len(result)

        # print "P %s" % len(p)

        # print result

        # return len(result)

        

        
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/0_todo
"""