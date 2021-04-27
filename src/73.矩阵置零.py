#
# @lc app=leetcode.cn id=73 lang=python
#
# [73] 矩阵置零
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        print(row, col)

        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        for j in col:
            for i in range(len(matrix)):
                matrix[i][j] = 0

# @lc code=end

