class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.insert(0, item)

    def remove(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)
