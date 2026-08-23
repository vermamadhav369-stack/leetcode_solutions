# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #first we taking Two pointers.
        slow = head
        fast = head

        #we are moving those pointers, so when fast is arrive at last node, slow is almost at middle node.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        #Odd length = middle element skips.
        if fast is not None:
            slow = slow.next

        #This loop helps to reverse the second half(from slow pointer to end node) of linked list and after completing the loop (prev_node) becomes the head of the reversed half.
        prev_node = None
        while slow is not None:
            front = slow.next
            slow.next = prev_node
            prev_node = slow
            slow = front

        #This loop help to compares the value of first half(from head to slow pointer) and second half(reversed half(from prev_node to end)) of the linked list.
        curr = head
        while prev_node is not None: #Reversed Half
            if curr.val != prev_node.val:
                return False
            curr = curr.next
            prev_node = prev_node.next

        return True
        