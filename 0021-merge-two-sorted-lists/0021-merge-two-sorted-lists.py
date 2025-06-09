class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2     
        dummy = ListNode(-1)
        tail = dummy
        
        while p1 and p2:  
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next
        
        tail.next = p1 if p1 else p2
        return dummy.next
        
        