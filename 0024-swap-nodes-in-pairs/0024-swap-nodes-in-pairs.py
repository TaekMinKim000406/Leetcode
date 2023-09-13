# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head  
        
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        
        while curr and curr.next:
            # 두 노드 스왑
            next_pair = curr.next.next
            prev.next = curr.next
            curr.next.next = curr
            curr.next = next_pair
            
            # 다음 반복을 위해 포인터 이동
            prev = curr
            curr = next_pair
        
        return dummy.next  

            