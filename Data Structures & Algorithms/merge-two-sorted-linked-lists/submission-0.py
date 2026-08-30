# Key takeaway: Create a dummy node to handle which list to pick 
# as the head

# have 1 pointer to actually make the list itself and 2 pointers to
# help compare the values at any given point

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Trying to code the recursive solution

        def helper(dummy: Optional[ListNode], list1: Optional[ListNode], list2: Optional[ListNode]):
            if list1 is None and list2 is None:
                dummy.next = None
                return
            
            if list1 is None:
                dummy.next = list2
                return

            if list2 is None:
                dummy.next = list1
                return

            if list1.val < list2.val:
                dummy.next = list1
                helper(dummy.next, list1.next, list2)
            else:
                dummy.next = list2
                helper(dummy.next, list1, list2.next)

        dummy = node = ListNode()

        helper(dummy, list1, list2)

        return node.next

        