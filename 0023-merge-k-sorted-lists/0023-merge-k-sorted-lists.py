# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # traverse lists to put first to minHeap: O(L)
        # while minHeap: O(N * L)
        # heappop(), put into result, put next elem to heap O(logL)
        # minHeap # (value, index ,node, nextNode)
        # tc: O(N * L * logL) / sc: O(L * L) include result
        
        minHeap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node, node.next))
        dummy = tail = ListNode()
        while minHeap:
            val, index, node, nxt = heapq.heappop(minHeap)
            tail.next = node
            tail = tail.next
            if nxt:
                heapq.heappush(minHeap, (nxt.val, index + len(lists), nxt, nxt.next))
        return dummy.next
        

