#
# @lc app=leetcode.cn id=572 lang=python
#
# [572] 另一个树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSametree(s, t):
            if not s and not t:
                return True
            elif not s or not t:
                return False
            if s.val == t.val:
                return isSametree(s.left, t.left) and isSametree(s.right, t.right)
        
        if not s and not t:
            return True
        if not s or not t:
            return False
        
        return isSametree(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right,t)
# @lc code=end

