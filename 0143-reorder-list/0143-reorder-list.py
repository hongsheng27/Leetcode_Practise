# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        # reverse
        prev = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        list1 = head
        list2 = prev
        # combine
        while list2:
            next1 = list1.next
            next2 = list2.next
            list1.next = list2
            list2.next = next1
            list1 = next1
            list2 = next2
        
      

        