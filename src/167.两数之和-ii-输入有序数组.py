#
# @lc app=leetcode.cn id=167 lang=python
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        i, j = 0, len(numbers)-1
        while i<j:
            sums = numbers[i]+numbers[j]
            if sums < target:
                i += 1
            if sums > target:
                j -= 1
            if sums == target:
                res.append(i+1)
                res.append(j+1)
                break
        return res
# @lc code=end

