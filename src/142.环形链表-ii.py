#
# @lc app=leetcode.cn id=142 lang=python
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        fast, slow = head, head
        while fast and slow:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    break
            else:
                return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
        
# @lc code=end

