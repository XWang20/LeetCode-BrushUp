#
# @lc app=leetcode.cn id=199 lang=python
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        queue = [root]
        res = []
        while queue:
            p = []
            for node in queue:
                if node.left:
                    p.append(node.left)
                if node.right:
                    p.append(node.right)
            res.append(queue[-1].val)
            queue = p
        return res
# @lc code=end

