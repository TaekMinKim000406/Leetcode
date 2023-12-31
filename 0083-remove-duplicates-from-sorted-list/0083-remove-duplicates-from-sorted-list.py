# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return

        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                if cur.next.next:
                    cur.next = cur.next.next
                else:
                    cur.next =None
            else:        
                cur = cur.next

        return head

        