# Last updated: 9/5/2025, 3:01:47 AM
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # pointer_1 = 0
        # pointer_2 = 0

        # while len(nums1) < m+n and pointer_2 < n:
        #     if nums1[pointer_1] <= nums2[pointer_2] and nums1[pointer_1+1] > nums2[pointer_2]:
        #         nums1.insert(pointer_1+1, nums2[pointer_2])
        #         pointer_2 += 1

        #     else:
        #         pointer_1 += 1

        
        # pointer_2 = 0

        # for i in range(m, m+n):
        #     nums1[i] = nums2[pointer_2]
        #     pointer_2 += 1

        pointer_1 = m - 1
        pointer_2 = n - 1
        pointer_merge = m + n - 1

        while pointer_2 >= 0:  # Keep merging until all nums2 elements are merged
            if pointer_1 >= 0 and nums1[pointer_1] > nums2[pointer_2]:
                nums1[pointer_merge] = nums1[pointer_1]
                pointer_1 -= 1
            else:
                nums1[pointer_merge] = nums2[pointer_2]
                pointer_2 -= 1
            
            pointer_merge -= 1