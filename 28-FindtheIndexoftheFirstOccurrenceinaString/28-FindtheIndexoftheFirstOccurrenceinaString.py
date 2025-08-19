# Last updated: 8/18/2025, 11:38:05 PM
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        len_needle = len(needle)
        i = 0

        if len(haystack) == len_needle:
            if haystack == needle:
                return 0
        
        while i <= len(haystack) - len_needle:
            sub_haystack = haystack[i:i+len_needle]
            if sub_haystack != needle:
                i += 1
            else:
                return i
        
        return -1

            