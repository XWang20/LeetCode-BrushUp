#
# @lc app=leetcode.cn id=387 lang=python
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        for i,j in enumerate(s):
            if counter[j] == 1:
                return i
        return -1
# @lc code=end

