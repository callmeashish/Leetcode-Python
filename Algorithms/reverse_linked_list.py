from typing import List

"""
206. Reverse Linked List

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ReverseList:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev


def makeLinkedListFromArray(arr: List[int]) -> ListNode:
    head = ListNode(arr[0])
    tail = head

    for i in arr[1:]:
        tail.next = ListNode(i)
        tail = tail.next

    return head


def printLinkedList(ll: ListNode) -> None:
    print_array = []
    while ll != None:
        print_array.append(ll.val)
        ll = ll.next
    print(print_array)


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5, 6]
    linked_list = makeLinkedListFromArray(head)
    removed_linked_list = ReverseList().reverseList(linked_list)
    printLinkedList(removed_linked_list)
