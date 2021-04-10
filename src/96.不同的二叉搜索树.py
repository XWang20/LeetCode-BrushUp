#
# @lc app=leetcode.cn id=96 lang=python
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        #dp[i]表示从1到i不同二叉搜索树的种类
        dp = [0] * (n+1)
        dp[0] = 1  # 空树也是一种二叉树搜索树
        for i in range(1, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
# @lc code=end

