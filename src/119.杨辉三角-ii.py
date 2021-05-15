#
# @lc app=leetcode.cn id=119 lang=python
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [0 for _ in range(rowIndex+1)]
        for i in range(rowIndex+1):
            res[i] = 1
            for j in range(i-1, 0, -1):
                res[j] += res[j-1]
        return res
# @lc code=end

