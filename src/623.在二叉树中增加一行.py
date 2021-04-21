#
# @lc app=leetcode.cn id=623 lang=python
#
# [623] 在二叉树中增加一行
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        queue = [root]
        i = 0
        if depth == 1:
            cur = root
            new = TreeNode(val)
            root = new
            new.left = cur
            return root

        while queue:
            i += 1
            if i == depth-1:
                last_layer = queue[:]
            q = []
            for node in queue:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            queue = q

        for node in last_layer:
            if node.left:
                new = TreeNode(val)
                cur = node.left
                node.left = new
                new.left = cur
            else:
                node.left = TreeNode(val)
            if node.right:
                new = TreeNode(val)
                cur = node.right
                node.right = new
                new.right = cur
            else:
                node.right = TreeNode(val)

        return root
# @lc code=end

