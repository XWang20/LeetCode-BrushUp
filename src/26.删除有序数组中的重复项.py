#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = i = 0
        length = len(nums)
        if length == 0 or length == 1:
            return length
        while i < length and j < length:
            if nums[i] == nums[j]:
                i += 1
            elif nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
                i += 1
        return j+1
# @lc code=end

