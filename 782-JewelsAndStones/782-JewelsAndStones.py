# Last updated: 6/19/2025, 11:46:27 AM
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """

        # stones_dict = {}

        # for i in range(len(stones)):
        #     if stones[i] in stones_dict:
        #         stones_dict[stones[i]] += 1
        #     else:
        #         stones_dict[stones[i]] = 1

        # print(stones_dict)

        # count = 0

        # for i in range(len(jewels)):
        #     if jewels[i] in stones_dict:
        #         count += stones_dict[jewels[i]]
        
        # return count

        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        
        return count

        