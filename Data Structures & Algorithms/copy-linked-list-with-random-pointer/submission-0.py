"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        hashmap = {}
        curr1 = head
        dummyNode = Node(0)
        prevNode = dummyNode

        while curr1: 
            print(curr1.random)
            newNode = Node(curr1.val)
            hashmap[curr1] = newNode
            prevNode.next = newNode
            prevNode = prevNode.next
            curr1 = curr1.next
        
        curr2 = head
        curr3 = dummyNode.next
        while curr2:
            if curr2.random is not None:
                curr3.random = hashmap[curr2.random]
            curr3 = curr3.next
            curr2 = curr2.next
        
        return dummyNode.next



        