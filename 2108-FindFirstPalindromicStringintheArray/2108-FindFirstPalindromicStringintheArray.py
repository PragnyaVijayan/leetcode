# Last updated: 9/18/2025, 11:36:18 PM
class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            s = str(word)
            if s == s[::-1]:
                return s
        return ""