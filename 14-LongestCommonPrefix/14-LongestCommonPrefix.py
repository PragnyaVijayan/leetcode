# Last updated: 7/8/2025, 11:35:38 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortest_string_index = min(range(len(strs)), key=lambda i: len(strs[i]))
        shortest_string = strs.pop(shortest_string_index)

        count = 0
        while count <= len(shortest_string):
            for string in strs:
                if string[0:count] != shortest_string[0:count]:
                    return shortest_string[0:count-1]
            count += 1
        print('final')
        return shortest_string

        




        