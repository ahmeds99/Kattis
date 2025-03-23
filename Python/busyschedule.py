import bisect
from functools import total_ordering


@total_ordering
class Time:
    def __init__(self, time_str, is_am):
        self.hour, self.minutes = [int(x) for x in time_str.split(":")]
        self.is_am = is_am

    def __eq__(self, value):
        return self.hour == value.hour and self.minutes == value.minutes

    def __lt__(self, other):
        if self.hour == other.hour:
            return self.minutes < other.minutes

        if self.hour == 12:
            return True
        elif other.hour == 12:
            return False

        return self.hour < other.hour

    def __str__(self):
        return f'{self.hour}:{self.minutes if self.minutes >= 10 else "0" + str(self.minutes)} {"a.m." if self.is_am else "p.m."}'

    def __repr__(self):
        return self.__str__()


num_lines = int(input())

while num_lines != 0:
    sorted_am = []
    sorted_pm = []
    a = []
    b = []

    for _ in range(num_lines):
        info = input().strip().split()
        is_am = info[1] == "a.m."

        bisect.insort(sorted_am if is_am else sorted_pm, Time(info[0], is_am))

    [print(x) for x in sorted_am]
    [print(x) for x in sorted_pm]
    print()
    num_lines = int(input())
