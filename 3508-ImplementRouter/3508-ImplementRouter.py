# Last updated: 9/20/2025, 11:14:46 PM
class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        brokenLetters = set(brokenLetters)
        count = 0
        for word in text.split():
            chars = set(word)
            if not (chars & brokenLetters):  
                count += 1
        return count

        