# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            kth = self.findKth(groupPrev, k)
            if not kth:
                break
            GroupNext = kth.next
            # reverse
            prev = kth.next
            cur = groupPrev.next
            while cur != GroupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

        

    def findKth(self, curr, k):
        while curr and k > 0:
            k -= 1
            curr = curr.next
        return curr

    