class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        '''
            if an opening bracket is encountered, append to stack
            if a closing bracket is encountered, pop it. 
                if anything besides the corresponding closing bracket is encountered, then return false
            check if stack is empty: return true else false
        '''

        parentheses_stack = []

        for character in s:
            if (character == '(' or character == '[' or character == '{'):
                parentheses_stack.append(character)
                #print(parentheses_stack)

            elif (character == ')' or character == ']' or character == '}'):
                if parentheses_stack:
                    #print(parentheses_stack)
                    if (character == ')' and parentheses_stack[-1] == '('):
                        parentheses_stack.pop()
                    elif (character == ']' and parentheses_stack[-1] == '['):
                        parentheses_stack.pop()
                    elif (character == '}' and parentheses_stack[-1] == '{'):
                        parentheses_stack.pop()
                    else:
                        return False
                else:
                    return False
                
        if parentheses_stack: # Checking to see if stack is empty
            return False
        else:
            return True
