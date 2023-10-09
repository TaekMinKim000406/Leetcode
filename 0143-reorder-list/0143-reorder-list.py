# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
          

        #한마디로 처음 끝 처음 끝 이순서로 접근해서 재구성
        node = head
        nodes = []
        while node:
            nodes.append(node)
            node = node.next

        left = 1
        right = len(nodes)-1
        turn = True
        node = head

        while left<=right:
            if turn:
                node.next = nodes[right]
                right -=1
                node = node.next
                turn = False
            else:
                node.next = nodes[left]
                left +=1
                node = node.next   
                turn = True

        node.next = None

