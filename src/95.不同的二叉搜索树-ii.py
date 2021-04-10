#
# @lc app=leetcode.cn id=95 lang=python
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        dct = {}

        def generateTree(left, right):
            if left > right:
                return [None]
            if (left, right) in dct:
                return dct[(left, right)]
            all_trees = []
            for i in range(left, right+1):
                left_list = generateTree(left, i-1)
                right_list = generateTree(i+1, right)
                for l in left_list:
                    for r in right_list:
                        cur_tree = TreeNode(i)
                        cur_tree.left = l
                        cur_tree.right = r
                        all_trees.append(cur_tree)
            dct[(left, right)] = all_trees
            return all_trees
        
        res = generateTree(1, n)
        return res

# @lc code=end

