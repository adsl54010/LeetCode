# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None and l2==None:
            return []
        elif l1==None:
            return l2
        elif l2==None:
            return l1
        if l1.val>l2.val:
            tmepans=ListNode(l2.val)
            if l2.next==None:
                tmepans.next=l1
                return tmepans
            else:
                l2=l2.next
        else:
            tmepans=ListNode(l1.val)
            if l1.next==None:
                tmepans.next=l2
                return tmepans
            else:
                l1=l1.next
        ans=tmepans
        while True:
            if l1.val>l2.val:
                NewNode=ListNode(l2.val)
                tmepans.next=NewNode
                tmepans=tmepans.next
                if l2.next==None:
                    NewNode.next=l1
                    return ans
                else:
                    l2=l2.next
            else:
                NewNode=ListNode(l1.val)
                tmepans.next=NewNode
                tmepans=tmepans.next
                if l1.next==None:
                    NewNode.next=l2
                    return ans
                else:
                    l1=l1.next
            
