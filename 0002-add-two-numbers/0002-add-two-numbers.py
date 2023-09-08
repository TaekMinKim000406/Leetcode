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
        num1 = ''
        num2 = ''
        while l1:
            num1+=str(l1.val)
            l1 = l1.next
        while l2:
            num2+=str(l2.val)
            l2 = l2.next

        
        result = int(num1[::-1])+int(num2[::-1])
        result = str(result)
        result = result[::-1]

        head = None
        temp = None
        for i in result:
            if not head:
                head = ListNode(i)
                temp = head
            else:
                temp.next = ListNode(i)
                temp = temp.next
        return head