# Last updated: 9/13/2025, 10:08:39 PM
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2_index = []
        for num1 in nums1:
            nums2_index.append(nums2.index(num1))
        
        #print(nums2_index)
        result = []
        
        for i in nums2_index:
            j = i + 1
            #print(i, j)
            result_count = len(result)
            while j < len(nums2):
                #print(nums2[j], nums2[i])
                if nums2[j] > nums2[i]:
                    #print('inside if')
                    result.append(nums2[j])
                    break
                j += 1

            if len(result) == result_count:
                result.append(-1)

            #print('result: ' , result)

        return result

            




        