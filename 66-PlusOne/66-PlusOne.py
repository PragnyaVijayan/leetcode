# Last updated: 8/27/2025, 11:27:40 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
         999 -> 1000
         99    (popped 1 time)
         9      (popped 2 times)


         4999 -> 5000
         499.    (popped 1)
         49      (popped 2)
         4       (popped 3)





        '''


        len_digits = len(digits)

        last_digit = digits[-1]

        if last_digit != 9:
            digits.pop()
            digits.append(last_digit + 1)
        else:
            count = 0
            while digits[-1] == 9 and len(digits) > 1:
                next_digit = digits.pop()
                count += 1
            if digits[-1] == 9:
                digits.pop()
                digits.append(1)
                digits.append(0)
            else:
                last_digit = digits.pop()
                digits.append(last_digit + 1)


            for _ in range(0, count):
                digits.append(0)
            
            print(digits)

        return digits
            
            



        