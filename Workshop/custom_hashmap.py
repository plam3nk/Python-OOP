class HashTable:

    def __init__(self):
        self.__capacity = 4
        self.__keys = [None] * self.__capacity
        self.__values = [None] * self.__capacity

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]

        except ValueError:
            raise KeyError(f"{key} is not a valid key.")

    def __setitem__(self, key, value):
        if len(self) == self.__capacity:
            self.__resize()

        index = self.__calc_index(key)
        index = self.__get_index(index)

        self.__keys[index] = key
        self.__values[index] = value

    def __calc_index(self, key):
        return sum(ord(c) for c in key) % self.__capacity

    def __get_index(self, index):
        if index == self.__capacity:
            index = 0

        if self.__keys[index] is None:
            return index

        return self.__get_index(index + 1)

    def __resize(self):
        self.__keys = self.__keys + [None] * self.__capacity
        self.__values = self.__values + [None] * self.__capacity
        self.__capacity *= 2

    def __len__(self):
        return len([k for k in self.__keys if k is not None])

    def add(self, key, value):
        self[key] = value

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def get_representation(self):
        print('{', end='')

        for i in range(self.__capacity):
            key = self.__keys[i]

            if key is not None:
                print(f'{key}: {self.__values[i]},', end=' ')

        print('}')


table = HashTable()

table.add('Ivan', 'Plamen')

table.get_representation()
print(table.get('Ivan'))