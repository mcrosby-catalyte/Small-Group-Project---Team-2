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


timestamps = [
    "2025-3-4 1:31:54 CDT",
    "2025-7-4 3:54:59 CDT",
    "2025-1-4 13:19:38 CDT",
    "2025-11-2 14:46:20 CDT",
    "2025-12-14 13:46:24 CDT",
    "2025-12-15 10:45:34 CDT",
    "2025-4-13 18:45:54 CDT",
    "2025-12-20 11:39:56 CDT",
    "2025-8-16 2:24:17 CDT",
    "2025-8-24 4:29:32 CDT",
    "2025-10-10 17:42:14 CDT",
    "2025-10-18 7:56:13 CDT",
    "2025-11-25 8:49:46 CDT",
    "2025-11-21 16:32:34 CDT",
    "2025-9-13 7:48:25 CDT",
    "2025-12-6 23:32:49 CDT",
    "2025-10-5 5:37:20 CDT",
    "2025-11-13 21:24:53 CDT",
    "2025-7-5 4:33:22 CDT",
    "2025-2-12 4:33:27 CDT",
    "2025-12-16 3:25:11 CDT",
    "2025-7-9 8:23:48 CDT",
    "2025-8-23 7:40:19 CDT",
    "2025-6-24 11:56:19 CDT",
    "2025-4-25 11:11:27 CDT",
    "2025-7-4 14:10:22 CDT",
    "2025-3-22 6:11:18 CDT",
    "2025-3-23 13:15:22 CDT",
    "2025-5-18 13:33:35 CD",
]


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

print(str(timestamps))
