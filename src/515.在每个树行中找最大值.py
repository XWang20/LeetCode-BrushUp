#
# @lc app=leetcode.cn id=515 lang=python
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        queue = [root]
        res = []
        while queue:
            q = []
            max_num = queue[0].val
            for node in queue:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                max_num = node.val if node.val>max_num else max_num

            queue = q
            res.append(max_num)

        return res
# @lc code=end

