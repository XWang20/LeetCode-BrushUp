#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # if head is None or head.next is None:
        #     return head
        # last = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return last

        if not head or not head.next:
            return head

        cur, pre = head, None
        while cur:
            next_code = cur.next
            cur.next = pre
            pre = cur
            cur = next_code

        return pre
# @lc code=end

