#
# @lc app=leetcode.cn id=637 lang=python
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = list()
        queue = [root]
        while queue:
            q = []
            total = 0
            for node in queue:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                total += node.val

            res.append(total/float(len(queue)))
            queue = q
        return res
            
# @lc code=end

