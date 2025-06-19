# Last updated: 6/19/2025, 11:46:29 AM
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        '''
        if first is 0 and next is 0, change
        if last is 0 and the one before is 0, change

        '''

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                if n <= 1:
                    return True
                else:
                    return False
            else:
                if n == 0:
                    return True
                else:
                    return False

        additionally_potted = 0

        for i in range(len(flowerbed)):
            if additionally_potted < n:
                if i == 0:
                    if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        additionally_potted += 1

                elif i == len(flowerbed) - 1:
                    if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                        print("last index", i)
                        flowerbed[i] = 1
                        additionally_potted += 1
                        if additionally_potted == n:
                            return True

                else:
                    if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        print("changed index: ", i)
                        flowerbed[i] = 1
                        additionally_potted += 1
            else:
                print('additionally potted before True: ', additionally_potted)
                return True

        print('additionally potted before False: ', additionally_potted)
        return False

        