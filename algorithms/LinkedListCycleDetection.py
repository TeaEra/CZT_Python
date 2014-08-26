#_*_ coding: utf-8 _*_

__author__ = 'TeaEra'

from DataStructure import ListNode


def detect_cycle(head):
    """
    [EN]

    [ZH]
    定理： 有定理：碰撞点p到连接点的距离=头指针到连接点的距离;
    因此，分别从碰撞点、头指针开始走，相遇的那个点就是连接点。
    """
    if not head or not head.next or not head.next.next:
        return None
    #
    one_step_pointer = head.next
    two_steps_pointer = head.next.next
    cycle_length = 1
    is_has_cycle = False
    while two_steps_pointer and one_step_pointer.next \
            and two_steps_pointer.next:
        if one_step_pointer == two_steps_pointer:
            is_has_cycle = True
            break
        one_step_pointer = one_step_pointer.next
        two_steps_pointer = two_steps_pointer.next.next
        cycle_length += 1
    if not is_has_cycle:
        return None
    temp_head = head
    while True:
        if temp_head == one_step_pointer:
            break
        temp_head = temp_head.next
        one_step_pointer = one_step_pointer.next
    return temp_head


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node2.next = node1
    #
    print(detect_cycle(node1).val)