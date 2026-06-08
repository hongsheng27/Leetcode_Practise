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
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        list2 = slow.next
        slow.next = None
        # reverse
        prev = None
        cur = list2
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # combination
        list1 = head
        list2 = prev
        while list2:
            nxt1 = list1.next
            nxt2 = list2.next
            list1.next = list2
            list2.next = nxt1
            list1 = nxt1
            list2 = nxt2
            