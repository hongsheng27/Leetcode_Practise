# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        minHeap = [] # val, i, node
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))
        dummy = tail = ListNode()
        while minHeap:
            v, i, n = heapq.heappop(minHeap)
            tail.next = n
            tail = tail.next
            if n.next:
                heapq.heappush(minHeap, (n.next.val, i, n.next))           
        return dummy.next

