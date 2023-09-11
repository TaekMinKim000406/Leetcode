# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        #cycle 생성
        total_length = 1
        tail = head
        while tail.next:
            tail = tail.next
            total_length += 1
        tail.next = head

        #현재 head위치에서 n-k만큼 이동하면 새로운 head
        #tail에서 마찬가지로 n-k만큼 이동하면 새로운 tail
        k = k%total_length
        for i in range(total_length-k):
            head = head.next
            tail = tail.next

        tail.next = None
        return head    




