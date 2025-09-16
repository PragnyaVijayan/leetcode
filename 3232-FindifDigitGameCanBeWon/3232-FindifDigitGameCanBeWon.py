# Last updated: 9/15/2025, 11:52:40 PM
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """

        letters = set(sentence)
        if len(letters) == 26:
            return True
        else:
            return False
        