# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1value = 0
        l2value = 0
        while l1:
            l1value = 10*l1value+l1.val
            l1 = l1.next
        while l2:
            l2value = 10*l2value+l2.val
            l2= l2.next    

        value = l1value+l2value
        head = None

        while value>0:
            node = ListNode(value%10)
            node.next,head = head, node
            value = value//10
        if head is None:
            return ListNode(0)

        return head
