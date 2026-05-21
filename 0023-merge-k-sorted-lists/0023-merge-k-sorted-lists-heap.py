# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = tail = ListNode(0)

        minHeap = []
        for i in range(len(lists)):
            if lists[i]:
                minHeap.append((lists[i].val, i, lists[i]))
        heapq.heapify(minHeap)

        while minHeap:
            [val, index, node] = heapq.heappop(minHeap)
            tail.next = node
            tail = tail.next
            newNode = node.next
            if newNode:
                heapq.heappush(minHeap, (newNode.val, index, newNode))
        return res.next





    