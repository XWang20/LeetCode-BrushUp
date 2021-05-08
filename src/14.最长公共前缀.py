#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""

        for i in range(len(strs[0])):
            c = strs[0][i]
            flag = True
            for j in range(len(strs)):
                if len(strs[j])-1<i or c != strs[j][i]:
                    flag = False
                    break
            if not flag:
                break
            else:
                res += c
        return res
            

# @lc code=end

