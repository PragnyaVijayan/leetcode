# Last updated: 9/18/2025, 11:23:11 PM
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
        