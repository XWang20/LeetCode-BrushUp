#
# @lc app=leetcode.cn id=653 lang=python
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        res = []
        inorder(root)
        for i in range(len(res)-1):
            if res[i] >= 0 and res[i] > k:
                return False
            for j in range(i+1, len(res)):
                if res[j] > k - res[i]:
                    break
                if res[j] + res[i] == k:
                    return True
        return False
# @lc code=end

