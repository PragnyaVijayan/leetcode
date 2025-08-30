# Last updated: 8/29/2025, 10:43:43 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
            for each cycle, fastpointer does next 2 times and slowpointer does it once
            if at any point fastpointer == slowpointer, then there is a cycle

        '''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None:
            return False

        slow_pointer = head
        fast_pointer = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                return True

        return False

