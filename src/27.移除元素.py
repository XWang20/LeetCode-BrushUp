#
# @lc app=leetcode.cn id=27 lang=python
#
# [27] 移除元素
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        low, fast = 0, 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[low] = nums[fast]
                low += 1
        return low
# @lc code=end

