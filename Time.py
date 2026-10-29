class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.convert_time()

    def convert_time(self):
        total = self.hours * 3600 + self.minutes * 60 + self.seconds
        self.hours = total // 3600
        self.minutes = (total % 3600) // 60
        self.seconds = total % 60

    def __add__(self, other):
        return Time(
            self.hours + other.hours,
            self.minutes + other.minutes,
            self.seconds + other.seconds
        )

    def increment(self):
        self.seconds += 1
        self.convert_time()

    def __gt__(self, other):
        time1 = self.hours * 3600 + self.minutes * 60 + self.seconds
        time2 = other.hours * 3600 + other.minutes * 60 + other.seconds
        return time1 > time2

    def __str__(self):
        return f"{self.hours}:{self.minutes:02}:{self.seconds:02}"


# Create two Time objects
t1 = Time(1, 50, 0)
t2 = Time(1, 20, 0)

# Add the two times
result = t1 + t2
print("Addition:", result)

# Increase t1 by one second
t1.increment()
print("After increment:", t1)

# Compare the two times
if t1 > t2:
    print("The first time is greater")
else:
    print("The second time is greater than or equal to the first")
