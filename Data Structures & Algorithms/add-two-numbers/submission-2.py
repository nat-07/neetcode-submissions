# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #go through each linked list and add
        #if adding goes up to 10, add one digit to the next in line

        #Create a dummy node
        final = ListNode()
        curr = final
        leftover = False

        while l1 and l2:
            if leftover: 
                total = l1.val + l2.val + 1
                leftover = False
            else: 
                total = l1.val + l2.val
            if total > 9: 
                leftover = True
                total = total - 10
            newNode = ListNode(total)
            curr.next = newNode
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            if leftover: 
                total = l1.val + 1
                leftover = False
            else:
                total = l1.val 
            if total > 9: 
                leftover = True
                total = total - 10
            newNode = ListNode(total)
            curr.next = newNode
            curr = curr.next
            l1 = l1.next
        
        while l2:
            if leftover: 
                total = l2.val + 1
                leftover = False
            else:
                total = l2.val
            if total > 9: 
                leftover = True
                total = total - 10
            newNode = ListNode(total)
            curr.next = newNode
            curr = curr.next
            l2 = l2.next

        if leftover:
            newNode = ListNode(1)
            curr.next = newNode
        return final.next


        
        