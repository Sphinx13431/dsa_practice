'''
Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
'''

class Node:
    def __init__(self,value:int):
        self.val=value
        self.next=None

class Solution:
    def partition_x(self,head:Node,x:int)->Node:
        small,large=Node(-1),Node(-1)
        ts,tl=small,large
        curr=head
        while curr:
            if(curr.val<x):
                ts.next=curr
                ts=ts.next
            else:
                tl.next=curr
                tl=tl.next
            curr=curr.next
        tl.next = None 
        ts.next=large.next
        return small.next
    
'''
tc is O(N)
space is O(1)
'''