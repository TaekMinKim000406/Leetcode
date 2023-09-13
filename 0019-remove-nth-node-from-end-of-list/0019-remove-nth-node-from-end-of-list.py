# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 1
        a = head
        while a.next:
            length +=1
            a = a.next


        cur =head
        for i in range(length - n-1):
            cur = cur.next
        next_node = cur.next
        
        if n == length:
            return head.next

        if next_node:
            next_node = next_node.next
            temp = cur.next
            temp.next = None
            cur.next = next_node
            return head

        