from typing import Optional
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        l1,l2=list1,list2
        tmp1,tmp2,tmp3=l1,l2,head
        while(tmp1 is not None and tmp2 is not None):
            if(tmp1.val <= tmp2.val):
                tmp3.next=tmp1
                tmp1=tmp1.next
            else:
                tmp3.next=tmp2
                tmp2=tmp2.next
            tmp3=tmp3.next
        
        if(tmp1 is not None):
            tmp3.next=tmp1
            
        if(tmp2 is not None):
            tmp3.next=tmp2
        
        head=head.next
        return head
    
# Helper function to convert list to linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper function to print linked list
def print_linkedlist(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)

l1 = list_to_linkedlist([1,2,3,4])
l2 = list_to_linkedlist([1,3,5])
sol = Solution()
merged = sol.mergeTwoLists(l1,l2)
print_linkedlist(merged)
                
        
        
        