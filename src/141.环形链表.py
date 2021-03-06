#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast and slow:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return True
            else:
                return False
        return False
        
# @lc code=end

