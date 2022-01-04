# leetcode problem
# Given a string s, find the length of the longest substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = []
        retVal = 0
        for x in s:
            if len(tmp) == 0 or not(x in tmp):
                tmp += x
                
            elif x in tmp:
                if len(tmp) == 1:
                    tmp = []
                    tmp += x
                
                else:
                    tmp = tmp[(tmp.index(x)+1):len(tmp)]
                    tmp += x
                
            
            if retVal < len(tmp):
                retVal = len(tmp)
            
        return retVal