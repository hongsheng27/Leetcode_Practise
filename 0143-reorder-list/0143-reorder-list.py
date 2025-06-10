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
        if not head:
            return
        lst = []
        cur = head
        while cur:
            lst.append(cur)
            cur = cur.next
        l, r = 0, len(lst) - 1
        while l < r:
            lst[l].next = lst[r]
            l += 1
            if l >= r: break
            lst[r].next = lst[l]
            r -= 1
        lst[r].next = None
        return lst[0]


        
