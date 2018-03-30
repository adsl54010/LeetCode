# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        tempans=head
        ans=tempans
        for i in range (1,n) :
            head=head.next
        if head.next==None :
            return tempans.next
        while head.next.next != None :
            head=head.next
            tempans=tempans.next
        tempans.next=tempans.next.next
        return ans
