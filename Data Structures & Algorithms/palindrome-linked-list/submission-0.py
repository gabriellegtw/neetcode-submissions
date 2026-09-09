# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        # Initially forgot to check fast.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # Reverse linked list
        dummy = None
        while slow:
            temp = slow.next
            slow.next = dummy
            dummy = slow
            slow = temp

        left = head
        # right should be dummy since this is the new start
        right = dummy

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
        