#
# @lc app=leetcode.cn id=557 lang=python
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        s = [word[::-1] for word in s]
        return ' '.join(s)
# @lc code=end

