#leetcode problem
# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab" or "aba"

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        elif len(s) == 1:
            return s
        else:
            start, end = 0, 0
            for x in range(len(s)):
                len1 = self.palindromeSeeker(s, x, x)
                len2 = self.palindromeSeeker(s, x, x + 1)
                length = max(len1, len2)

                if length > end - start:
                    start = x - (length - 1) / 2;
                    end = x + length / 2

            return s[start:end+1]

    def palindromeSeeker(self, s, l, r):
        L, R = l, r
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1

        return R - L - 1

# In order to find the palindrome, I used the algorithm which expand around char of every index in array
# It takes O(n) time to go through the "s" string and takes O(n) time to expand around char of every index of array to find palindrome
# So that the total time complexity is O(n^2)