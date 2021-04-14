#
# @lc app=leetcode.cn id=404 lang=python
#
# [404] 左叶子之和
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(root, flag):
            if not root:
                return
            if not root.left and not root.right:
                if flag:
                    self.total += root.val
                    return
                else:
                    return
            
            dfs(root.left, 1)
            dfs(root.right,0)
        
        dfs(root, 0)
        return self.total
# @lc code=end

