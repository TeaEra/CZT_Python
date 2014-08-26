__author__ = 'TeaEra'

from DataStructure import ListNode
from DataStructure import create_nodes
from DataStructure import show_nodes


def delete_duplicates(head):
    if not head or not head.next:
        return head
    # TODO: ???

if __name__ == "__main__":
    #
    print("---")
    node1 = create_nodes([2, 3, 3])
    show_nodes(delete_duplicates(node1))