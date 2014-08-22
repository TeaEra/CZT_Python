__author__ = 'TeaEra'

from DataStructure import ListNode
from DataStructure import create_nodes
from DataStructure import show_nodes


def sort_list(head):
    # TODO: not finished;
    """

    1. sorted_less_last is None;
    2. sorted_less_last.next is None, should break;
    3. Time Limit Exceeded: a very long input;
    """
    if (not head) or (not head.next):
        return head
    pivot = head
    pointer = head.next
    less_head = ListNode(-1)
    more_head = ListNode(-1)
    less_pointer = less_head
    more_pointer = more_head
    while pointer:
        if pivot.val > pointer.val:
            less_pointer.next = pointer
            less_pointer = less_pointer.next
        else:
            more_pointer.next = pointer
            more_pointer = more_pointer.next
        pointer = pointer.next
    less_pointer.next = None
    more_pointer.next = None
    sorted_less_part = sort_list(less_head.next)
    sorted_more_part = sort_list(more_head.next)
    sorted_less_last = sorted_less_part
    while sorted_less_last:
        if sorted_less_last.next:
            sorted_less_last = sorted_less_last.next
        else:
            break
    if sorted_less_last:
        sorted_less_last.next = pivot
        pivot.next = sorted_more_part
        return sorted_less_part
    pivot.next = sorted_more_part
    return pivot

if __name__ == "__main__":
    created_head = create_nodes([2, 4])
    show_nodes(created_head)
    sorted_head = sort_list(created_head)
    show_nodes(sorted_head)