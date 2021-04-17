#
# @lc app=leetcode.cn id=530 lang=python
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        res = []
        inorder(root)
        return min([abs(res[i] - res[i+1]) for i in range(len(res)-1)])
# @lc code=end

