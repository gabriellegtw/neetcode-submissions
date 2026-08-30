# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = a = b = head
        stack = []

        while b:
            stack.append(b)
            b = b.next

        n = len(stack)

        b = stack.pop()

        for _ in range(n // 2):
            temp = a.next
            a.next = b
            a = temp
            b.next = a
            b = stack.pop()

        a.next = None

            