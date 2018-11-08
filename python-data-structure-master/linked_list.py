class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next_link):
        self.next = next_link

    def __str__(self):
        return 'NODE data: {}; NODE next: {}'.format(self.data, self.next)


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        temp = Node(value)
        temp.set_next(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, value):
        current = self.head
        found = False

        while current is not None and not found:
            if current.get_data() == value:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, value):
        current = self.head
        previous = None
        found = False

        while current is not None and not found:
            if current.get_data() == value:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current is None:
            self.head = previous.get_next()
        else:
            previous.set_next(current.get_next())

    def __str__(self):
        return str(self.head)
