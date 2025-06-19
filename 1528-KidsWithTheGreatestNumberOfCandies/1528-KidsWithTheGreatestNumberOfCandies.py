# Last updated: 6/19/2025, 11:46:24 AM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        '''
            get the max of all the numbers
            if list[i] + extra > max then true
            else false
        '''

        max_candies = max(candies)
        boolean_array = []

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                boolean_array.append(True)
            else:
                boolean_array.append(False)
        
        return boolean_array

        