# Last updated: 7/8/2025, 9:42:04 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        letter_hash = {}

        for i in s:
            if i not in letter_hash:
                letter_hash[i] = 1
            else:
                letter_hash[i] = letter_hash[i] + 1

        for j in t:
            if j in letter_hash:
                if letter_hash[j] >= 1:
                    letter_hash[j] = letter_hash[j] - 1
                else:
                    return False
            else:
                return False

        if all(not values for values in letter_hash.values()):
            return True
        else:
            return False
        