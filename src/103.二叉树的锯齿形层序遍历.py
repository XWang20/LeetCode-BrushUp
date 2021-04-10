#
# @lc app=leetcode.cn id=103 lang=python
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = [root]
        res = []
        flag = True
        while queue:
            q = []
            p = []
            for node in queue:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not flag: # flag为True时从左到右遍历
                queue.reverse()
            for node in queue:
                p.append(node.val)
            flag = not flag
            res.append(p)
            queue = q
        return res
# @lc code=end

