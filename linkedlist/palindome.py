'''
Palindrome: Implement a function to check if a linked list is a palindrome.
'''

class ListNode:
    def __init__(self, value: int):
        self.val = value
        self.next = None

class Solution:
    def find_middle_node(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_from_middle(self, middle: ListNode) -> ListNode:
        prev = None
        curr = middle
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val

        middle_node = self.find_middle_node(head)
        rev_head = self.reverse_from_middle(middle_node)

        first, second = head, rev_head
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True
