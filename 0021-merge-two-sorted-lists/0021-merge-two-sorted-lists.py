class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2     
        dummy = ListNode(-1)
        tail = dummy
        
        while p1 and p2:  
            if not p1:
                tail.next = p2
                break
            elif not p2:
                tail.next = p1
                break

            if p1.val <= p2.val:
                tail.next = p1
                tail = p1
                p1 = p1.next
            else:
                tail.next = p2
                tail = p2
                p2 = p2.next
        
        if p1:
            tail.next = p1
        else:
            tail.next = p2
            
        return dummy.next
            
            
            

                
            
        # p1 < p2 => p1 head
        # p1 + 1

        
        