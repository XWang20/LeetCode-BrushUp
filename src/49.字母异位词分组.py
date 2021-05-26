#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashtable = {}
        for s in strs:
            alpha = ''.join(sorted(s))
            if alpha in hashtable:
                hashtable[alpha].append(s)
            else:
                hashtable[alpha] = [s]
        return list(hashtable.values())
# @lc code=end

