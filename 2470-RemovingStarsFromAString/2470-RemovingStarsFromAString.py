# Last updated: 6/19/2025, 11:46:22 AM
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        '''
            edge cases:
                - the number of stars is more than the number of letters on the left
                - the length is 1
                    - only star
                    - only letter
                - 
        
        
        '''

        final_string = []
        
        for character in s:
            #print(''.join(final_string))
            if character == '*':
                if final_string:
                    final_string.pop()
            else:   
                final_string.append(character)

        return ''.join(final_string)
        