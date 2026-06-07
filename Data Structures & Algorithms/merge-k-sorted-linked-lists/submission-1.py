# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        min_heap = []

        for i in range(0, len(lists)):
            heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
    
        dummy = ListNode()
        head = dummy

        while min_heap:
            popedEle = heapq.heappop(min_heap)
            if popedEle[2].next:
                heapq.heappush(min_heap,(popedEle[2].next.val, popedEle[1], popedEle[2].next))

            dummy.next = popedEle[2]
            dummy = dummy.next

        return head.next





        