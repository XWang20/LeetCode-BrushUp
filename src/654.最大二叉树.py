#
# @lc app=leetcode.cn id=654 lang=python
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        max_num = max(nums)
        root = TreeNode(max_num)
        mid = nums.index(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:mid])
        root.right = self.constructMaximumBinaryTree(nums[mid+1:])

        return root
# @lc code=end

