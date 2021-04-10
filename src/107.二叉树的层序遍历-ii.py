#
# @lc app=leetcode.cn id=107 lang=python
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            p = []
            q = []
            for node in queue:
                q.append(node.val)
                if node.left:
                    p.append(node.left)
                if node.right:
                    p.append(node.right)
            res.append(q)
            queue = p
        res.reverse()
        return res
# @lc code=end

