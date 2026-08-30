# Key takeaway: For recursion, call the recursive funcction first before 
# Doing the key action because if you do the key action first (i.e. reversing)
# Then the code will break as it is a cycle

# To return a linked list, return its head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        currentNode = head
        while currentNode:
            # Do not need this line as you will create a cycle
            # currentNode.next.next = currentNode
            temp = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = temp
        return prev
                
        