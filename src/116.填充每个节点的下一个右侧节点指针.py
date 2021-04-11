#
# @lc app=leetcode.cn id=116 lang=python
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def dfs(root):
            if not root:
                return None
            right = root.right
            left = root.left
            while left:
                left.next = right
                left = left.right
                right = right.left
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return root
        
# @lc code=end

