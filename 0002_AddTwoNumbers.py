# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Approach:
        1. Adds number from head to tail, consider the carry over
           e.g.
           
           *
           6 -> 8 -> 9
           7 -> 5 -> 8 -> 4 -> 3
        -------------------------
           3 -> 4 -> 8 -> 5 -> 3
        
        2. Add new linkedlist res to store
        '''
        dummy = ListNode()
        res = dummy
        carry = 0

        # Loop while there's l1, l2, or carry
        while l1 or l2 or carry:
            # Get value of l1 and l2
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            # Do addition and handles carry
            suml1l2 = carry + l1val + l2val
            carry = suml1l2 // 10
            suml1l2 = suml1l2 % 10

            # Create new node
            res.next = ListNode(suml1l2)

            # Move to next node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            res = res.next
        
        return dummy.next
