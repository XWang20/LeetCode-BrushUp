#
# @lc app=leetcode.cn id=217 lang=python
#
# [217] 存在重复元素
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashtable = set()
        for num in nums:
            if num in hashtable:
                return True
            else: 
                hashtable.add(num)
        return False
# @lc code=end

