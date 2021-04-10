#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def dfs(root, left, right):

            if not root:
                return True

            if left < root.val < right:
                return True and dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
            
            else:
                return False
        
        return dfs(root, -float('inf'), float('inf'))

# @lc code=end

