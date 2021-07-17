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


class BinaryLinkedToInt:
    def getDecimalValueArithmetic(self, head: ListNode) -> int:
        decimal_value = 0
        while head:
            decimal_value = decimal_value * 2 + head.val
            head = head.next

        return decimal_value

    def getDecimalValueBitwise(self, head: ListNode) -> int:
        decimal_value = 0
        while head:
            decimal_value <<= 1
            if head.val:
                decimal_value += 1
            head = head.next

        return decimal_value


if __name__ == "__main__":

    linked_list = arrayToList([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])

    print(BinaryLinkedToInt().getDecimalValueBitwise(linked_list))
