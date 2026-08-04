# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        curr = head

        while curr:
            counter += 1
            curr = curr.next

        counter -= n

        # Remove the head
        if counter == 0:
            return head.next

        prev = None
        curr = head

        for _ in range(counter):
            prev = curr
            curr = curr.next

        prev.next = curr.next

        return head

        