#
# @lc app=leetcode.cn id=113 lang=python
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        def sum(root, targetSum):
            
            if not root:
                return
            path.append(root.val)
            targetSum -= root.val
            if not root.left and not root.right and not targetSum:
                res.append(path[:])

            sum(root.left, targetSum)
            sum(root.right, targetSum)
            path.pop() # 

        sum(root,targetSum)
        return res
# @lc code=end

