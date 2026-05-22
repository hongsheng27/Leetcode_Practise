
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:  
        dummy = prevGroupTail = ListNode(0, head)
        while True:
            kth = prevGroupTail
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # reverse
            groupNext = kth.next
            prev = groupNext
            cur = prevGroupTail.next
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            tmp = prevGroupTail.next
            prevGroupTail.next = prev
            prevGroupTail = tmp
        
        
        
