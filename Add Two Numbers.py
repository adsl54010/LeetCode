# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp=ListNode(0)
        ans=temp
        carry=0
        if l1 :
            carry +=l1.val
            l1=l1.next
        if l2 :
            carry +=l2.val
            l2=l2.next
        carry,temp.val=divmod(carry,10)
        while l1 or l2 or carry:
            if l1 :
                carry +=l1.val
                l1=l1.next
            if l2 :
                carry +=l2.val
                l2=l2.next
            temp.next=ListNode(carry)
            temp=temp.next
            carry,temp.val=divmod(carry,10)
        return ans
