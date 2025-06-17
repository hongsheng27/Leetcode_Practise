# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            list1, list2 = lists[0], lists[1]
            dummy = tail = ListNode()
            while list1 and list2:
                if list1.val <= list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            tail.next = list1 or list2
            lists[0] = dummy.next
            lists.pop(1)
        return lists[0] if len(lists) > 0 else None

            
        