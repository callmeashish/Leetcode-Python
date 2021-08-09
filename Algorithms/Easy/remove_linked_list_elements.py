from typing import List

"""
203. Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class RemoveElements:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        main_list = ListNode(0)
        tail = main_list
        while head != None:
            if head.val != val:
                tail.next = ListNode(head.val)
                tail = tail.next
            head = head.next
        return main_list.next


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
    head = [1, 2, 6, 3, 4, 5, 6]
    target = 6
    linked_list = makeLinkedListFromArray(head)
    removed_linked_list = RemoveElements().removeElements(linked_list, target)
    printLinkedList(removed_linked_list)
