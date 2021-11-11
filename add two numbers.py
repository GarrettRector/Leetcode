# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
       result_head = ListNode(0)
       current = result_head
       c = 0
       while (l1 is not None or l2 is not None):
           a = 0
           b = 0
           if l1 is not None:
               a = l1.val
           if l2 is not None:
               b = l2.val
           if a + b + c >= 10:
               val = (a + b + c) % 10
               c = 1
           else:
               val = a + b + c
               c = 0
           current.val = val
           if l1 is not None:
               l1 = l1.next
           if l2 is not None:
               l2 = l2.next
           if l1 is not None or l2 is not None:
               current.next = ListNode(0)
               current = current.next
           elif l1 is None and l2 is None and c != 0:
               current.next = ListNode(c)
               current = current.next
       return result_head
