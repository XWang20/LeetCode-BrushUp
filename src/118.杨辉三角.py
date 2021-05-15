#
# @lc app=leetcode.cn id=118 lang=python
#
# [118] 杨辉三角
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1, numRows+1):
            if i == 1:
                res.append([1])
                continue
            lastRow = res[-1]
            newRow = [0 for _ in range(i)]
            newRow[0] = newRow[-1] = 1
            for j in range(1, i-1):             
                newRow[j] = lastRow[j-1]+lastRow[j]
            res.append(newRow)
        return res
# @lc code=end

