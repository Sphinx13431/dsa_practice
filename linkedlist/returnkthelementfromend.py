'''
Return Kth to Last: Implement an algorithm to find the kth to last element 
of a singly linked list.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def kth_to_last(self, head: Node, k: int) -> Node:
        if not head:
            return None

        slow = fast = head

        # Move fast k steps ahead
        for _ in range(k):
            if not fast:
                # k is greater than the length of the list
                return None
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        return slow  # kth-to-last node
