from typing import List


"""
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class IsPalindrome:
    # Using Stacks
    def isPalindrome1(self, head: ListNode) -> bool:
        slow = head
        stack = []

        while slow != None:
            stack.append(slow.val)
            slow = slow.next

        while head != None:
            i = stack.pop()
            if i != head.val:
                return False
            head = head.next
        return True

    # Reversing the linked list
    def isPalindrome2(self, head: ListNode) -> bool:
        length = 0
        temp = head

        while temp != None:
            length += 1
            temp = temp.next

        leftHalf = None
        rightHalf = head

        i = 0
        while i < int(length / 2):
            temp = rightHalf
            rightHalf = rightHalf.next
            temp.next = leftHalf
            leftHalf = temp
            i += 1

        rightHalf = rightHalf if length % 2 == 0 else rightHalf.next

        while rightHalf != None and leftHalf != None:
            if rightHalf.val != leftHalf.val:
                return False
            rightHalf = rightHalf.next
            leftHalf = leftHalf.next

        return True


def linked_list_to_array(arr: List[int]) -> ListNode:
    head = ListNode(arr[0])
    temp = head
    for i in arr[1:]:
        temp.next = ListNode(i)
        temp = temp.next

    return head


if __name__ == "__main__":
    head = [1, 2, 2, 1]
    linked_list = linked_list_to_array(head)
    print(IsPalindrome().isPalindrome1(linked_list))
    print(IsPalindrome().isPalindrome2(linked_list))
