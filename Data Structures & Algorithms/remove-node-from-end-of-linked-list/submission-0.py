# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        # Fast and slow pointers initialized to dummy
        fast = dummy
        slow = dummy

        # Creates n step delay between fast and slow pointers
        for i in range(n):
            fast = fast.next

        # Move pointers until fast pointer reaches end of list
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Assigns slow.next to the next of the nth node
        # Essentially deleting the nth node
        slow.next = slow.next.next

        # Return the head of the list
        return dummy.next