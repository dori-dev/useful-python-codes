"""create a custom range link python range() function
"""


class Range:
    """Create a object like range object
    """

    def __init__(self, start: int, stop: int = None, step: int = 1):
        if stop is None:
            stop, start = start, 0
        self.start = start
        self.stop = stop
        self.step = step
        self.index = -1
        if start < stop and step > 0:
            self.iterable = self.make_forewark_iterable()
        elif start > stop and step < 0:
            self.iterable = self.make_backward_iterable()
        else:
            self.iterable = []
        self.length = len(self.iterable)

    def make_forewark_iterable(self):
        """make iterable for foreward iterate

        Returns:
            list: iterable list
        """
        iterable = []
        start = self.start
        stop = self.stop
        step = self.step
        while start < stop:
            iterable.append(start)
            start += step
        return iterable

    def make_backward_iterable(self):
        """make iterable for backward iterate

        Returns:
            list: iterable list
        """
        iterable = []
        start = self.start
        stop = self.stop
        step = self.step
        while start > stop:
            iterable.append(start)
            start += step
        return iterable

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < self.length:
            return self.iterable[self.index]
        raise StopIteration()

    def __len__(self):
        return len(self.iterable)

    def __repr__(self):
        if self.step == 1:
            return f'Range({self.start}, {self.stop})'
        return f'Range({self.start}, {self.stop}, {self.step})'


# test Range works!
print(len(Range(1, 10)) == len(range(1, 10)))
my_counter = Range(10, 1, -1)
print(my_counter.iterable == list(range(10, 1, -1)))

for counter_num, range_num in zip(Range(10, 30, 5), range(10, 30, 5)):
    print(counter_num == range_num)

my_counter = Range(10, 21, -2)
my_range = range(10, 21, -2)
print(my_counter.iterable == list(my_range))
print(len(my_counter) == len(my_range))
