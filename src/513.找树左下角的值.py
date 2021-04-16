#
# @lc app=leetcode.cn id=513 lang=python
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        queue = [root]
        while queue:
            q = []
            left = queue[0].val
            for node in queue:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            queue = q
        return left
# @lc code=end

