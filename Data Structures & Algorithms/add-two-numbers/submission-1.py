# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode(0)
        dummy = result

        first = l1
        second = l2
        carry = 0

        while first != None or second != None:
            if first == None:
                firstVal = 0
            else:
                firstVal = first.val

            if second == None:
                secondVal = 0
            else:
                secondVal = second.val

            addn = firstVal + secondVal + carry
            if addn > 9:
                carry = 1
                addn = addn % 10
            else:
                carry = 0

            dummy.next = ListNode(addn)
            dummy = dummy.next

            if first != None:
                first = first.next 

            if second != None:
                second = second.next

        if carry == 1:
            dummy.next = ListNode(1)

        return result.next
            
        