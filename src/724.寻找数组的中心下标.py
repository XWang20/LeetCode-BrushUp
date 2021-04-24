#
# @lc app=leetcode.cn id=724 lang=python
#
# [724] 寻找数组的中心下标
#

# @lc code=start
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        start = 0
        for i in range(len(nums)):
            if start*2 + nums[i] == total:
                return i
            start += nums[i]
        return -1
# @lc code=end

