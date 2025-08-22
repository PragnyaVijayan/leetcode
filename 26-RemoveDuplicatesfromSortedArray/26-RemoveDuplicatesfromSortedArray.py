# Last updated: 8/21/2025, 11:01:27 PM
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        - fast and slow pointer approach
        - slow pointer will be before duplicates. can insert there
        - if fast pointer reaches end of loop, everything between slow 
            and fast pointer is '_'
        '''

        '''
        1  1  2  2  3  4
        ||

        1  1  2  2  3  4
        |  |

        1  2  2  2  3  4
           |  |

        1  2  2  2  3  4
           |     |

        1  2  3  2  3  4
              |     |

        1  2  3  4  3  4
                 |     |

        '''

        fast_pointer = 0
        slow_pointer = 0
        original_len = len(nums)
        
        #print(nums)

        while fast_pointer < original_len - 1:
            if nums[fast_pointer] != nums[fast_pointer + 1]:
                slow_pointer += 1
                nums[slow_pointer] = nums[fast_pointer + 1]

            # print('nums :', nums)
            # print('fast pointer: ', fast_pointer)
            # print('slow pointer: ', slow_pointer)

            fast_pointer += 1

        if len(nums) > original_len:
            for i in range(slow_pointer+1, original_len):
                nums[i] = '-'
            
            for i in range(original_len+1, len(nums)):
                nums.pop()

        #print(slow_pointer + 1)
        #print(nums)
        return slow_pointer + 1
        

        