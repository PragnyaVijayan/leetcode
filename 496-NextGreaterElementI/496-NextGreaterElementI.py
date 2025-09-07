# Last updated: 9/6/2025, 10:35:07 PM
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        '''
            step 1: implement a monotonic stack for nums2 (called next_greatest)
            step 2: for each element in nums1, lookup next_greatest

        '''

        next_greatest = []
        stack = []
        nums2 = nums2[::-1]

        for num in nums2:
            while stack and stack[-1] <= num:
                stack.pop()
            
            if not stack:
                next_greatest.append(-1)
            else:
                next_greatest.append(stack[-1])
            
            stack.append(num)

        print(nums2)
        print(stack)
        print(next_greatest)

        ans = []
        for num in nums1:
            #print(num)
            index = nums2.index(num)
            #print(index)
            temp = next_greatest[index]
            #print(temp)
            ans.append(temp)
        
        return ans




        