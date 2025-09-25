# Last updated: 9/24/2025, 11:49:34 PM
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """

        max_count = 0

        for sentence in sentences:
            word_list = sentence.strip().split()
            count = len(word_list)

            if max_count < count:
                max_count = count
        
        return max_count
        