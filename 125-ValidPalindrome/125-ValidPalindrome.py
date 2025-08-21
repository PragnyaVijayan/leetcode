# Last updated: 8/21/2025, 8:47:03 AM
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        print(s)
        s = s.lower()
        s = "".join([char for char in s if char.isalnum() is True])
        print(s)

        forward_pointer = 0
        backward_pointer = len(s) - 1

        is_palindrome = True

        # if len(s) == 1:
        #     return False

        while forward_pointer < backward_pointer:
            if s[forward_pointer] == s[backward_pointer]:
                forward_pointer += 1
                backward_pointer -= 1
            else:
                return False

        return is_palindrome
            
        