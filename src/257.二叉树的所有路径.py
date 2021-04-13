#
# @lc app=leetcode.cn id=257 lang=python
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def path(root, s):
            if not root:
                return
            if not s:
                s = "%d"%(root.val)
            else:
                s = s + "->%d"%(root.val)
            if not root.left and not root.right:
                res.append(s)
            path(root.left, s)
            path(root.right, s)
        res = []
        path(root, "")
        return res
# @lc code=end

