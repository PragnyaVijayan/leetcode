# Last updated: 6/19/2025, 11:46:24 AM
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        i = 0
        merged_array = []

        while i < len(word1) and i < len(word2):
            merged_array.append(word1[i])
            merged_array.append(word2[i])
            i += 1
        
        if len(word1) > len(word2):
            while i < len(word1):
                merged_array.append(word1[i])
                i += 1

        else:
            while i < len(word2):
                merged_array.append(word2[i])
                i += 1
        
        return "".join(merged_array)

