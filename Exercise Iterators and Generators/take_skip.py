class take_skip():

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.start = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.counter < self.count:
            current_number = self.start
            self.counter += 1
            self.start += self.step
            return current_number

        else:
            raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)





