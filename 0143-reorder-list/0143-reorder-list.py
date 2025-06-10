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
        lst = []
        cur = head
        while cur:
            lst.append(cur)
            cur = cur.next
        l, r = 0, len(lst) - 1
        dummy = tail = ListNode()
        while l <= r:
            if l != r:
                lst[l].next = lst[r]
                tail.next = lst[l]
                tail = tail.next.next
            else:
                tail.next = lst[l]
                tail = tail.next
            tail.next = None
            l += 1
            r -= 1
        return dummy.next


        
