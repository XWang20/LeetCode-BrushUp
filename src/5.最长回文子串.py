#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            # 奇数情况
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # 偶数情况
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
    
    def helper(self, s, l, r):
        while l >=0 and r < len(s) and s[l]==s[r]:
            l -= 1; r += 1
        return s[l+1:r]
# @lc code=end

