# Last updated: 9/3/2025, 11:51:58 PM
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        '''
            [10, 4, 8, 3]
            [0]

            [10, 4, 8, 3]
            [0,3]

            [10, 4, 8, 3]
            [0,3,11]

            [10, 4, 8, 3]
            [0,3,11,15] -> [15,11,3,0]


            [10, 4, 8, 3]
            []


        '''


        left_Sum = []
        left_Sum.append(0)

        reverse_num = nums[::-1]
        right_Sum = []
        right_Sum.append(0)

        for i in range(1,len(nums)):
            left_Sum.append(left_Sum[i-1] + nums[i-1])
            right_Sum.append(right_Sum[i-1] + reverse_num[i-1])
            #print(right_Sum)

        right_Sum = right_Sum[::-1]

        difference = list(map(lambda x, y: abs(x - y), left_Sum, right_Sum))
        return(difference)



        