"""
160. Intersection of Two Linked Lists

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.


Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
0 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
 

Follow up: Could you write a solution that runs in O(n) time and use only O(1) memory?
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Intersect:
    # Algorithmic Approach
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        length1 = 0
        length2 = 0

        node = headA
        while node != None:
            length1 += 1
            node = node.next

        node = headB
        while node != None:
            length2 += 1
            node = node.next

        nodeA = headA
        nodeB = headB

        if length2 > length1:
            nodeA = headB
            nodeB = headA

        i = 0
        while i < abs(length1 - length2):
            nodeA = nodeA.next
            i += 1

        while nodeA != None and nodeB != None:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next

        return None

    # Map Approach
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        mydict = {}
        temp1 = headA
        temp2 = headB
        while temp1:
            mydict[temp1] = temp1.val
            temp1 = temp1.next
        while temp2:
            if temp2 in mydict:
                return temp2
            temp2 = temp2.next


if __name__ == "__main__":

    ll1 = ListNode(4)
    ll1.next = ListNode(1)

    ll2 = ListNode(5)
    ll2.next = ListNode(6)
    ll2.next.next = ListNode(1)

    ll3 = ListNode(8)
    ll3.next = ListNode(4)
    ll3.next.next = ListNode(5)

    ll1.next.next = ll3
    ll2.next.next.next = ll3

    print((Intersect().getIntersectionNode1(ll1, ll2)).val)
    print((Intersect().getIntersectionNode2(ll1, ll2)).val)
