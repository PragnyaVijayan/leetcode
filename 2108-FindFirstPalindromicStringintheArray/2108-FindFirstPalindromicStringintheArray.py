# Last updated: 9/18/2025, 11:35:07 PM
class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            forward_pointer, reverse_pointer = 0, len(word) - 1
            is_palindrome = True

            while forward_pointer < reverse_pointer:
                if word[forward_pointer] != word[reverse_pointer]:
                    is_palindrome = False
                    break
                forward_pointer += 1
                reverse_pointer -= 1

            if is_palindrome:
                return word

        return ""