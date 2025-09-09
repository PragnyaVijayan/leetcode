# Last updated: 9/8/2025, 10:37:49 PM
class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        diagonal_length = []
        max_length = float('-inf')
        for dimension in dimensions:
            length = sqrt(dimension[0] * dimension[0] + dimension[1] * dimension[1])
            diagonal_length.append(length)

            if length > max_length:
                max_length = length

        area = []
        
        for i, diagonal_len in enumerate(diagonal_length):
            if diagonal_len == max_length:
                area.append(dimensions[i][0] * dimensions[i][1])
        
        return max(area)
        


        