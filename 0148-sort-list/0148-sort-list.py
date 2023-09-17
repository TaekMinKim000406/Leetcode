# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next ==None:
            return head

        values = []
        while head.next:
            values.append(head.val)
            head = head.next
        values.append(head.val)

        values.sort()

        dummy_head = ListNode(0)
        cur = dummy_head
        for i in range(len(values)):
            cur.next = ListNode(values[i])
            cur = cur.next
        return dummy_head.next