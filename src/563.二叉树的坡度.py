#
# @lc app=leetcode.cn id=563 lang=python
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.total = 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            return left + right + root.val

        if not root:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)
        self.total += abs(left - right)

        self.findTilt(root.left)
        self.findTilt(root.right)

        return self.total
        
# @lc code=end

