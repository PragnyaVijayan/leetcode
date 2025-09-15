# Last updated: 9/14/2025, 11:22:39 PM
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        letter_frequency = {}
        for char in s:
            if char not in letter_frequency:
                letter_frequency[char] = 1
            else:
                letter_frequency[char] += 1
            
        for i in range(0, len(s)):
            if s[i] in letter_frequency and letter_frequency[s[i]] == 1:
                return i
            
        return -1
        