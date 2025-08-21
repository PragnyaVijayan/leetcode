# Last updated: 8/21/2025, 4:50:24 PM
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        '''
            - for the firt two it has 1 & 1,1 respectively
            - following that, 1's on each end
            - sliding window of 2
        '''

        triangle = []

        for i in range(1, numRows + 1):
            j = 0
            row_numbers = []
            while j < i:
                row_numbers.append(1)
                j += 1
            triangle.append(row_numbers)
            #print(triangle)

        for i in range(2, numRows):
            previous_row_length = i

            temp = []
            j = 0
            while j < previous_row_length - 1:
                #print(triangle[i-1][j], triangle[i-1][j+1])
                #temp.append(triangle[i-1][j] + triangle[i-1][j+1])
                triangle[i][j+1] = triangle[i-1][j] + triangle[i-1][j+1]
                j += 1
            
            #print(i)
            #print(temp)
            #print(triangle)

        return triangle


        