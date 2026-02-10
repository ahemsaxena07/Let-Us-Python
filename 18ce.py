class time:
    def __init__(self):
        self.h = int(input("enter the hour: "))
        self.m = int(input("etner the min: "))

    def inputdata(self, other):
        other.h = int(input("enter the hour: "))
        other.m = int(input("etner the min: "))

    def display(self, other):
        total_minute = self.m + other.m
        time_hour = self.h + other.h + (total_minute // 60) 
        time_hour = time_hour % 24
        min_hour = total_minute % 60

        diff_min = self.m - other.m
        diff_hour = self.h - other.h 
        diff_hour = diff_hour % 24
        if diff_min < 0:
            diff_hour = diff_hour - 1  # borrow 1 hour
            diff_min = diff_min + 60 
        print(f"time after subtraction- {diff_hour}:{diff_min}")
        print(f"time after addition- {time_hour}:{min_hour}")

time1 = time()
time2 = time()
time1.display(time2)

