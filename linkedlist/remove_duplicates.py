'''
remove duplicates: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
'''

'''
Clarifying qns
Is it a SLL or DLL
'''

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class Solution:
    def delete_brute(self, head:Node)->Node:
        if not head or not head.next:#if the ll has 0 or 1 Node
            return head
        curr=head
        while curr and curr.next:
            temp_before,temp_after=curr,curr.next
            while temp_after:
                if(curr.value==temp_after.value):
                    temp_after=temp_after.next
                    temp_before.next=temp_after
                else:
                    temp_before=temp_after
                    temp_after=temp_after.next
            curr=curr.next
        return head

    '''
      tc  O(N^2)
      sc O(1)
    '''



    def delete_better(self, head:Node)->Node: 
        if not head or not head.next:#if the ll has 0 or 1 Node
            return head
        my_set=set()
        my_set.add(head.value)
        before,after=head,head.next
        while after:
            if after.value in my_set:
                before.next=after.next
            else:
                my_set.add(after.value)
                before=after
            after=after.next
        return head
    '''
      tc  O(N)
      sc O(N)
    '''                
