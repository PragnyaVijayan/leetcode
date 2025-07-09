# Last updated: 7/8/2025, 9:47:51 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): # O(n)
            return False
        
        letter_hash_s = {}
        letter_hash_t = {}

        for i in s: # O(n)
            if i not in letter_hash_s:
                letter_hash_s[i] = 1
            else:
                letter_hash_s[i] = letter_hash_s[i] + 1
        
        for i in t: # O(n)
            if i not in letter_hash_t:
                letter_hash_t[i] = 1
            else:
                letter_hash_t[i] = letter_hash_t[i] + 1

        if letter_hash_s == letter_hash_t: # O(1)
            return True
        else:
            return False

        # for j in t: # O(n)
        #     if j in letter_hash:
        #         if letter_hash[j] >= 1:
        #             letter_hash[j] = letter_hash[j] - 1
        #         else:
        #             return False
        #     else:
        #         return False

        # if all(not values for values in letter_hash.values()): # O(n)
        #     return True
        # else:
        #     return False

        #return True
        