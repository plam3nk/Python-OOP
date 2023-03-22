class countdown_iterator():
    def __init__(self, count: int):
        self.count = count
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.count:
            raise StopIteration

        self.start += 1

        return self.count - self.start


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")

