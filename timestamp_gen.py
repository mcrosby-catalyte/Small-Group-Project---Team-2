import re
import random


class Timestamp:
    def __init__(self, year, month, day, hour, minute, second, zone):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.zone = zone

    def __repr__(self):
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second} {self.zone}\n"


timestamps = []


for i in range(15):
    timestamps.append(
        Timestamp(
            2025,
            random.randint(1, 12),
            random.randint(1, 25),
            random.randint(1, 24),
            random.randint(10, 59),
            random.randint(10, 59),
            "CDT",
        )
    )

print(timestamps)
