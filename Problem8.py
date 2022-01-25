# Leetcode problem
# Reverse Integer

# Input: x = 123
# Output: 321
# Input: x = -123
# Output: -321

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >= 2 ** 31 - 1 or x <= -2 ** 31:
            return 0
        else:
            tmpStr = str(x)
            if x >= 0:
                retVal = tmpStr[::-1]
            else:
                tmp = tmpStr[1:]
                tmp2 = tmp[::-1]
                retVal = "-" + tmp2
            if int(retVal) >= 2 ** 31 - 1 or int(retVal) <= -2 ** 31:
                return 0
            else:
                return int(retVal)