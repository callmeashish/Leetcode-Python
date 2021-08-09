"""
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DeleteDuplicates:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        root = ListNode(head.val)
        temp = root
        head = head.next
        while head != None:

            if temp.val != head.val:
                temp.next = ListNode(head.val)
                temp = temp.next

            head = head.next

        return root


def makeLinkedListFromArray(arr: List[int]) -> ListNode:
    root = ListNode(arr[0])
    temp = root
    for i in arr[1:]:
        temp.next = ListNode(i)
        temp = temp.next
    return root


def printLinkedList(ll: ListNode) -> None:
    arr = []

    while ll != None:
        arr.append(ll.val)
        ll = ll.next

    print(arr)


if __name__ == "__main__":
    arr = [1, 1, 2, 3, 3]
    ll = makeLinkedListFromArray(arr)
    printLinkedList(ll)
    removed_ll = DeleteDuplicates().deleteDuplicates(ll)
    printLinkedList(removed_ll)
