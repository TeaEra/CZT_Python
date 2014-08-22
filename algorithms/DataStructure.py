__author__ = 'TeaEra'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_nodes():
    nodes = list()
    for i in range(10, 0, -1):
        nodes.append(ListNode(i))
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    #
    pointer = nodes[0]
    return pointer


def create_nodes(int_arr):
    nodes = list()
    for i in range(len(int_arr)):
        nodes.append(ListNode(int_arr[i]))
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    #
    pointer = nodes[0]
    return pointer


def show_nodes(head1):
    p1 = head1
    print_res = ""
    while p1:
        print_res += str(p1.val)
        p1 = p1.next
        if p1:
            print_res += " -> "
    print(print_res)

if __name__ == "__main__":
    p = create_nodes()
    while p:
        print(p.val)
        p = p.next
