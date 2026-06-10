# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = tail = ListNode(0, None)
        minHeap = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(minHeap, (lst.val,i ,lst))
        while minHeap:
            value, index, node = heapq.heappop(minHeap)

            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val,index,node.next))
        return dummy.next
            