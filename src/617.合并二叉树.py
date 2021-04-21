#
# @lc app=leetcode.cn id=617 lang=python
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        def dfs(root1, root2):
            if not root1 and not root2:
                return
            elif not root2 and root1:
                dfs(root1.left, root2)
                dfs(root1.right, root2)
            elif root1 and root2:
                root1.val += root2.val
                if not root1.left and root2.left:
                    root1.left = TreeNode(0)
                if not root1.right and root2.right:
                    root1.right = TreeNode(0)
                dfs(root1.left, root2.left)
                dfs(root1.right, root2.right)
            else:
                return
        
        if not root1 and root2:
            return root2

        dfs(root1, root2)
        return root1
# @lc code=end

