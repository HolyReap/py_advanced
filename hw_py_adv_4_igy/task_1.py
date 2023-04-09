class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.go_on = True

    def __iter__(self):
        self.counter_i = 0
        self.counter_j = 0
        return self

    def __next__(self):
        if self.go_on:
            while self.counter_i < len(self.list_of_list):
                if self.counter_j < len(self.list_of_list[self.counter_i]):
                    item = self.list_of_list[self.counter_i][self.counter_j]
                    self.counter_j += 1
                    return item
                self.counter_i += 1
                self.counter_j = 0
            self.go_on = False
        raise StopIteration

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
