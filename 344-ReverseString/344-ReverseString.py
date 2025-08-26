# Last updated: 8/26/2025, 1:21:25 AM
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        forward_pointer = 0
        reverse_pointer = len(s) - 1
        
        while forward_pointer < reverse_pointer:
            temp = s[forward_pointer]
            s[forward_pointer] = s[reverse_pointer]
            s[reverse_pointer] = temp
            
            forward_pointer += 1
            reverse_pointer -= 1
            
        