# Last updated: 8/22/2025, 11:34:22 PM
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal = []

        for i in range(numRows):
            row = [1] * (i + 1) 
            #print(row)
            for j in range(1, i):
                row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
            pascal.append(row)

        return pascal