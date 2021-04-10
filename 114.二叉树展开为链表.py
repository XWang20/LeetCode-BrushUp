#
# @lc app=leetcode.cn id=114 lang=python
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        def preorder(root):
            if not root:
                return None
            res.append(root)
            preorder(root.left)
            preorder(root.right)
        res = []
        preorder(root)
        for i in range(len(res)-1):
            res[i].right = res[i+1]
            res[i].left = None
        res[len(res)-1].right = None
# @lc code=end

