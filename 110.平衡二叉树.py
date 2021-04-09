#
# @lc app=leetcode.cn id=110 lang=python
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def hight(root):
            if not root:
                return 0
            return max(hight(root.left)+1, hight(root.right)+1)

        left_hight = hight(root.left)
        right_hight = hight(root.right)

        if -1 <= (left_hight - right_hight) <= 1:
            return True and self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
# @lc code=end

