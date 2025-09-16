# Last updated: 9/15/2025, 11:56:12 PM
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """

        number_of_words = []
        for sentence in sentences:
            word_list = sentence.strip().split()
            #print(word_list)
            number_of_words.append(len(word_list))
        
        max_words = max(number_of_words)
        
        return max_words
        

        