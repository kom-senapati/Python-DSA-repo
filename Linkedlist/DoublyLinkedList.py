class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self) -> dict:
        return f"Node({dict(Value=self.value, Next=self.next, Prev=self.prev)})"

    def points(self, node) -> None:
        self.next = node
        node.prev = self


class Dll:
    def __init__(self, *elements) -> None:
        self.head = None

        for e in elements:
            self.append(e)

    def __repr__(self) -> str:
        a = self.head
        s = "Head -> "
        while a:
            s += f"{str(a.value)} <- -> "
            a = a.next
        s += str(None)
        return s

    def isempty(self):
        return self.head is None

    def append(self, e):
        n = Node(e)
        if self.isempty():
            self.head = n
        else:
            a = self.head
            while a.next:
                a = a.next
            a.points(n)

    def prepend(self, e):
        n = Node(e)
        if not self.isempty():
            n.points(self.head)
        self.head = n

    def insert(self, index, e):
        if index == 0 and self.isempty():
            self.append(e)
        elif index == 0:
            self.prepend(e)
        else:
            try:
                n = Node(e)
                a = self.head
                for _ in range(index - 1):
                    a = a.next
                n.points(a.next)
                a.points(n)
            except AttributeError:
                raise IndexError

    def pop(self):
        a = self.head
        while a.next.next:
            a = a.next
        popped = a.next
        a.next = None
        return popped

    def BegDelete(self):
        a = self.head
        self.head = a.next
        a.next = None

    def remove(self, key):
        a = self.head
        while a.next.value != key:
            a = a.next
        key = a.next
        a.points(key.next)
        key.next = (None)

    def reverse(self):
        prev = Node(None)
        curr = self.head
        while curr:
            Next = curr.next
            curr.next = prev
            prev.prev = curr
            prev = curr
            curr = Next
        self.head = prev
        self.pop()


dl = Dll(1, 2, 3, 4)
print(dl)
dl.reverse()
print(dl)
