#
# @lc app=leetcode.cn id=173 lang=python
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.res.append(root.val)
            inorder(root.right)

        self.res = []
        inorder(root)
        self.node = -1

    def next(self):
        """
        :rtype: int
        """
        self.node += 1
        return self.res[self.node]


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.node+1 < len(self.res):
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

