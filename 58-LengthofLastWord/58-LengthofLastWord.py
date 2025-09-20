# Last updated: 9/19/2025, 11:49:01 PM
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        reverse_string = s[::-1]
        reverse_string = reverse_string.strip()
        #print(reverse_string)
        last_word = reverse_string.partition(' ')[0]
        #print(last_word)
        # if last_word == " ":
        #     last_word = reverse_string.partition(' ')[2]

        return len(last_word)
        