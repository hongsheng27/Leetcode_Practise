# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 123 # 54
        dummy = slow = fast = ListNode(0, head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        slow.next = None
        # reverse back
        list2 = None
        while cur:
            nxt = cur.next
            cur.next = list2
            list2 = cur
            cur = nxt
        # concate
        newDummy = tail = ListNode()
        list1 = dummy.next
        while list1 and list2:
            nxt1 = list1.next
            nxt2 = list2.next

            tail.next = list1
            list1.next = list2
            tail = list2
            
            list1 = nxt1
            list2 = nxt2
        tail.next = list1 or list2
        return newDummy.next




        
        