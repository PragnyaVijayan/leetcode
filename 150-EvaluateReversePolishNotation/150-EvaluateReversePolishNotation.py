# Last updated: 6/19/2025, 11:46:32 AM
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        '''
        - if two numbers come in, put them into a stack. when operator comes, evaluate
        - put the number back into the stack
        - repeat
        '''
        
        tokens_stack = []

        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                tokens_stack.append(int(token))
            else:
                if len(tokens_stack) >=2: 
                    num1 = tokens_stack.pop()
                    num2 = tokens_stack.pop()

                    if token == "+":
                        tokens_stack.append(num1 + num2)
                    
                    elif token == "-":
                        tokens_stack.append(num2 - num1)

                    elif token == "*":
                        tokens_stack.append(num1 * num2)

                    elif token == "/":
                        if num1 != 0:
                            tokens_stack.append(int(float(num2) / float(num1)))
                        else:
                            raise Exception('Division by 0')
                    
        return tokens_stack[0]
