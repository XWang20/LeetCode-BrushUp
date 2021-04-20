#
# @lc app=leetcode.cn id=606 lang=python
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ""
        res = str(t.val)
        if t.left:
            res += "("
            res += self.tree2str(t.left)
            res += ")"
            if t.right:
                res += "("
                res += self.tree2str(t.right)
                res += ")"
        else:
            if t.right:
                res += "()("
                res += self.tree2str(t.right)
                res += ")"
        return res

# @lc code=end

