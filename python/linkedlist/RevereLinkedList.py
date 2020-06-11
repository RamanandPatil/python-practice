# Given a singly linked list, return another linkedlist that is the
# reverse of the first.
# Helper Code


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])


def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    new_linked_list = LinkedList()
    previous_node = None
    for value in linked_list:
        current_node = Node(value)
        current_node.next = previous_node
        previous_node = current_node

    new_linked_list.head = previous_node

    return new_linked_list
