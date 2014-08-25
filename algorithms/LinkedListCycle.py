__author__ = 'TeaEra'

from DataStructure import ListNode


def has_cycle(head):
    if not head or not head.next or not head.next.next:
        return False
    #
    one_step_pointer = head.next
    two_steps_pointer = head.next.next
    while two_steps_pointer and one_step_pointer.next \
            and two_steps_pointer.next:
        if one_step_pointer == two_steps_pointer:
            return True
        one_step_pointer = one_step_pointer.next
        two_steps_pointer = two_steps_pointer.next.next
    return False

if __name__ == "__main__":
    node1 = ListNode(0)
    node2 = ListNode(0)
    node3 = ListNode(0)
    node1.next = node1
    node2.next = node3
    node3.next = node2
    #
    print(has_cycle(node1))