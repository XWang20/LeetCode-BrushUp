#
# @lc app=leetcode.cn id=209 lang=python
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = right = 0
        minlength = len(nums)+1
        sumv = 0
        while right < len(nums):
            sumv += nums[right]
            while sumv >= target:
                minlength = min(right-left+1, minlength)
                sumv -= nums[left]
                left += 1
            right += 1

        if minlength > len(nums):
            return 0
        else:
            return minlength
# @lc code=end

