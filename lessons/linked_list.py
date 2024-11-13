from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(
        self, value: int, next: Node | None
    ):  # magic method called when an object is being initialized on the heap for the first time
        self.value = value
        self.next = next

    def __str__(
        self,
    ) -> (
        str
    ):  # method that is called automatically on any object when you try to convert something to a str in python
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        # TODO: Figure out the rest of the list
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(201, None)))


def to_str(head: Node | None) -> str:
    """Represent a linked list as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # Base Case: When head is the last node
    # return its value!
    #Recursive case:
    # Figure out the last node (recursive call)
    # in the "rest of the list"
    # Return this value!
    if head == 
    return -1


print(last(one))  # expect to print 2
print(last(courses))  # expect to print 301
