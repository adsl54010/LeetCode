# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        def divsorted(l,r):
            ans=tempans=ListNode(0)
            while l and r :
                if l.val>r.val:
                    tempans.next=r
                    tempans=tempans.next
                    r=r.next            
                else:
                    tempans.next=l
                    tempans=tempans.next
                    l=l.next                  
            if r:
                tempans.next=r
            else:
                tempans.next=l
            return ans.next
                            
                    
        if len(lists)==0:
            return []
        while len(lists)>1:
            tempspace=[]
            while len(lists)>1:                
                sort1=lists.pop()
                sort2=lists.pop()
                tempspace.append(divsorted(sort1,sort2))
            lists+=tempspace
        if len(lists)==0:
            return []
        return lists[0]
