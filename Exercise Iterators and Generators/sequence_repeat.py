class sequence_repeat():
    def __init__(self, sequence: str, length: int):
        self.sequence = sequence
        self.length = length
        self.index = -1
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.length:
            raise StopIteration

        if self.index >= len(self.sequence) - 1:
            self.index = -1

        self.counter += 1
        self.index += 1
        return self.sequence[self.index]


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

