# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)

        def helper(head, val):
            if head.next is None:
                return

            if head.next.val == val:
                temp = head.next.next
                head.next = temp
                helper(head, val)
            else:
                helper(head.next, val)

        helper(dummy, val)

        return dummy.next

        