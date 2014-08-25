__author__ = 'TeaEra'

from DataStructure import create_nodes
from DataStructure import show_nodes


def remove_duplicates_from_array(arr):
    if not arr or len(arr) == 1:
        return arr
    res_arr = list()
    res_arr.append(arr[0])
    idx = 0
    for i in range(1, len(arr)):
        if arr[i] != res_arr[idx]:
            res_arr.append(arr[i])
            idx += 1
    return res_arr


def delete_duplicates(head):
    if not head or not head.next:
        return head
    res_head = head
    last_node = res_head
    pointer = head.next
    while pointer:
        if pointer.val != last_node.val:
            last_node.next = pointer
            last_node = last_node.next
        pointer = pointer.next
    last_node.next = None
    return res_head

if __name__ == "__main__":
    #
    #print(remove_duplicates_from_array([1, 1, 2]))
    #print(remove_duplicates_from_array([1, 1, 2, 3, 3]))
    #
    head1 = create_nodes([1, 1, 2])
    head2 = create_nodes([1, 1, 2, 3, 3])
    print("---")
    show_nodes(delete_duplicates(head1))
    print("---")
    show_nodes(delete_duplicates(head2))