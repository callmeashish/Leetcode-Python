# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list_to_array(ll: ListNode) -> list:
    array = []
    while ll:
        array.append(ll.val)
        ll = ll.next
    return array


def arrayToList(arr):
    head = ListNode(arr[0])
    tail = head
    for i in arr[1:]:
        tail.next = ListNode(i)
        tail = tail.next
    return head


class MergeTwoLists:
    # Leman Solution
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummyHead = ListNode(0)
        curr = dummyHead

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = ListNode(l1.val)
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                curr = curr.next
                l2 = l2.next

        if l1:
            while l1:
                curr.next = ListNode(l1.val)
                curr = curr.next
                l1 = l1.next

        if l2:
            while l2:
                curr.next = ListNode(l2.val)
                curr = curr.next
                l2 = l2.next

        return dummyHead.next

    # Recursive harder to understand Solution
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == "__main__":

    l1 = [-9, 3]
    l2 = [5, 7]

    ll1 = arrayToList(l1)
    ll2 = arrayToList(l2)

    merged_ll = MergeTwoLists().mergeTwoLists(ll1, ll2)
    print(linked_list_to_array(merged_ll))
