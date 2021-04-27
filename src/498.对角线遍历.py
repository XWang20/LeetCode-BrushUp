#
# @lc app=leetcode.cn id=498 lang=python
#
# [498] 对角线遍历
#

# @lc code=start
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []
        res = []
        i,j = 0,0
        n,m = len(mat),len(mat[0])
        while True:
            res.append(mat[i][j])
            if i>=n-1 and j>=m-1:break
            if i%2==j%2:
                if j<m-1:
                    j=j+1
                    i=i-1 if i>0 else i
                else:i=i+1
            else:
                if i<n-1:
                    i=i+1
                    j=j-1 if j>0 else j
                else:j=j+1
        return res
# @lc code=end

