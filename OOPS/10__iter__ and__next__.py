# Task 10: __iter__ and __next__ (Custom Iterator Task)
# Problem Statement:
# Create a class Counter.
# Requirements:
# Initialize with start and end.
# Implement:
# __iter__()
# __next__()
# Task:
# Use in loop:
# for i in Counter(1, 5):
#     print(i)
# Expected Output:
# 1
# 2
# 3
# 4
# 5


class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # object itself is the iterator

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


# Using in a loop
for i in Counter(1, 5):
    print(i)
