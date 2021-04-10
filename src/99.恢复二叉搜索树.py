#
# @lc app=leetcode.cn id=99 lang=python
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        nums = []

        def Search(root):

            if not root:
                return None

            Search(root.left)
            nums.append(root)
            Search(root.right)

        Search(root)
        x , y = None, None

        pre = nums[0]

        for i in range(1, len(nums)):
            
            if pre.val > nums[i].val:
                y=nums[i]
                if not x:
                    x = pre
            pre = nums[i]
        if x and y:
            x.val, y.val = y.val, x.val
        
        return root

# @lc code=end

