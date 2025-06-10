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
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        l, r = 0, len(nodes) - 1
        while True:
            nodes[l].next = nodes[r]
            l += 1
            if l >= r: break
            nodes[r].next = nodes[l]
            r -= 1
        nodes[r].next = None



        
