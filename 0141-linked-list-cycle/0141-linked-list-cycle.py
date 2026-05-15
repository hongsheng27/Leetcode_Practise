# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = second = head
        while head and first:
            if first.next:
                first = first.next
            else: return False
            if second.next and second.next.next:
                second = second.next.next
            else: return False

            if first == second: return True
        return False
        