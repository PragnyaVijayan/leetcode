# Last updated: 6/19/2025, 11:46:30 AM
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        '''
        - need to know vowels, as well as the indices
        - traversing the word once, take count of all the vowels and indices
        - loop after and change in place. pop after each change
        '''

        #s = s.lower()

        vowels_stack = []
        index_stack = []

        for c in range(len(s)):
            if s[c] in "aeiouAEIOU":
                vowels_stack.append(s[c])
                index_stack.append(c)
            else:
                pass

        if not vowels_stack:
            return s

        print(index_stack)
        print(vowels_stack)

        s = list(s)

        for i in range(len(index_stack)):
            index = index_stack[i]
            reversed_vowel = vowels_stack[-(i + 1)]  # Access vowels in reverse order
            s[index] = reversed_vowel

        print(s)
        return "".join(s) 

                
