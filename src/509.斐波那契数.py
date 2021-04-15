#
# @lc app=leetcode.cn id=509 lang=python
#
# [509] 斐波那契数
#

# @lc code=start
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        f1 = 0
        f2 = f3 = 1
        if n < 1:
            return 0

        for _ in range(n-1):
            f3 = f1+f2
            f1 = f2
            f2 = f3

        return f3


# @lc code=end

