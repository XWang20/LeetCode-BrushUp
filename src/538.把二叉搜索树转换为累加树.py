#
# @lc app=leetcode.cn id=538 lang=python
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def inorder(root):
            if not root:
                return None
            inorder(root.right)
            root.val += self.total
            self.total = root.val
            inorder(root.left)

        inorder(root)
        return root
        
# @lc code=end

