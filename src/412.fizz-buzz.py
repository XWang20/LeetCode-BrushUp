#
# @lc app=leetcode.cn id=412 lang=python
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fb = []
        for i in range(1, n+1):
            if not i%15:
                fb.append('FizzBuzz')
            elif not i%3:
                fb.append('Fizz')
            elif not i%5:
                fb.append('Buzz')
            else:
                fb.append('%d'%i)
        return fb
# @lc code=end

