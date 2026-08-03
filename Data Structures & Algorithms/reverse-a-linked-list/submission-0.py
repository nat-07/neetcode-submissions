# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
          # Since this is a linked list, we do not know where the end is, so we first need to traverse through the list until the end. 
        # We could potentially have a stack that stores all of the nodes and pops them in order when we traverse the nodes again. 

        #Edgecase: if head is empty, return it
        if head is None: 
            return head
        
        #Step 1: Go through the list and populate the stack
        temp = head
        stack = []
        while temp.next is not None: 
            stack.append(temp.val)
            temp = temp.next 
        stack.append(temp.val)

        #Step 2: Go through the list again and pop the stack
        temp = head
        while bool(stack):
            temp.val = stack.pop()
            temp = temp.next
        return head


        