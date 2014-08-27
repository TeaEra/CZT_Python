__author__ = 'TeaEra'

from DataStructure import ListNode
from DataStructure import create_nodes
from DataStructure import show_nodes


def delete_duplicates(head):
    if not head or not head.next:
        return head
    prev = ListNode(-1)
    fake_head = prev
    pointer = head
    while pointer and pointer.next:
        if pointer.val != pointer.next.val:
            prev.next = pointer
            pointer = pointer.next
            continue
        while pointer.val == pointer.next.val:
            pointer = pointer.next
        pointer = pointer.next
    return fake_head.next

if __name__ == "__main__":
    #
    print("---")
    node1 = create_nodes([2, 2, 3])
    show_nodes(delete_duplicates(node1))