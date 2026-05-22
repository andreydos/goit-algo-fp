class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def sort(self):
        self.head = merge_sort(self.head)

    def to_list(self):
        values = []
        current = self.head

        while current is not None:
            values.append(current.data)
            current = current.next

        return values

    @classmethod
    def from_list(cls, values):
        linked_list = cls()
        for value in values:
            linked_list.append(value)
        return linked_list


def split_list(head):
    if head is None or head.next is None:
        return head, None

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    middle = slow.next
    slow.next = None
    return head, middle


def merge_sorted_lists(left, right):
    dummy = Node(0)
    tail = dummy

    while left is not None and right is not None:
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    if left is not None:
        tail.next = left
    else:
        tail.next = right

    return dummy.next


def merge_sort(head):
    if head is None or head.next is None:
        return head

    left, right = split_list(head)
    left = merge_sort(left)
    right = merge_sort(right)
    return merge_sorted_lists(left, right)


def merge_two_sorted_linked_lists(list1, list2):
    result = LinkedList()
    result.head = merge_sorted_lists(list1.head, list2.head)
    return result


def print_linked_list(title, linked_list):
    print(f"{title}: {linked_list.to_list()}")


if __name__ == "__main__":
    numbers = LinkedList.from_list([7, 3, 5, 1, 9, 2])
    print_linked_list("Original list", numbers)

    numbers.reverse()
    print_linked_list("Reversed list", numbers)

    numbers.sort()
    print_linked_list("Sorted list", numbers)

    first = LinkedList.from_list([1, 4, 6, 10])
    second = LinkedList.from_list([2, 3, 7, 8])
    merged = merge_two_sorted_linked_lists(first, second)
    print_linked_list("Merged sorted list", merged)
