# Last updated: 6/19/2025, 11:46:36 AM
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Think about spaces at the end after the last word

        # i = 0
        # space_index = -100

        # if len(s) == 1 or len(s) == 0:
        #     return len(s)

        # while i != len(s)-1:
        #     #print("i in while loop: ", i)
        #     character = s[i]
        #     next_character = s[i+1]
        #     if character == " " and next_character != " ":
        #         space_index = i # Will capture the last space
        #     i += 1

        # #print(space_index)

        # count = 0

        # for i in range (space_index + 1, len(s)):
        #     #print("i in for loop: ", i)
        #     if s[i] != " ":
        #         count += 1
        #     else:
        #         break
        
        # return count

        last_word_index = -100
        first_word_index = -100

        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                last_word_index = i
                break

        for i in range(last_word_index, -1, -1):
            print(i)
            if i == 0 and s[i] != " ":
                #print('in i == 0')
                first_word_index = i
                break

            if s[i] == " ":
                #print('checking')
                first_word_index = i + 1
                break
            
        
        print(first_word_index, " ", s[first_word_index])
        print(last_word_index, " ", s[last_word_index])

        return last_word_index - first_word_index + 1

        


        