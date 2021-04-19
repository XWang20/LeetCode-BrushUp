#
# @lc app=leetcode.cn id=543 lang=python
#
# [543] 二叉树的直径
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
        self.max = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_depth(root):
            if not root:
                return 0
            return max(max_depth(root.left), max_depth(root.right)) + 1

        if not root:
            return 0
        max_num = max_depth(root.left) + max_depth(root.right)
        self.max = max_num if max_num>self.max else self.max
        self.diameterOfBinaryTree(root.left) 
        self.diameterOfBinaryTree(root.right)

        return self.max
        
# @lc code=end

