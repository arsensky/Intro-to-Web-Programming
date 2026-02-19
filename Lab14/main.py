from datetime import datetime

current_time = datetime.now()
print("Current date and time:", current_time)
print(f"Current hour and minute: {current_time.hour}:{current_time.minute}")

specific_date = datetime(2022, 12, 18, 22, 30, 0)
print("Specific date:", specific_date)

formatted_date = specific_date.strftime("%H:%M:%S, %d/%m/%Y, %A, %B")
print("Formatted date:", formatted_date)

date_str = "01-02-2026 3:35:05"
date_obj = datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")
print("Parsed date object:", date_obj)

from datetime import timedelta

future_date = current_time + timedelta(days=7)
print("Future date:", future_date)

past_date = current_time - timedelta(days=3)
print("Past date:", past_date)

event_date = datetime(2005, 10, 21)
days_passed = current_time - event_date
print("Days have passed:", days_passed.days)

### Practical Examples
# 1. Creating a Calendar
import calendar
year = 2026
month = 2
print(calendar.month(year, month))

# 2. Countdown
import time

def countdown(seconds):
    while seconds:
        print("Time remaining:", seconds, "seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

countdown(1)

# 3. Measuring Execution Time
start_time = time.time()
sum(range(1, 1000001))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")

### Lab Exercises
# 1. Displaying the Current Date and Time
now = datetime.now()
formatted_now = now.strftime("%H:%M:%S, %d/%m/%Y")
print("Current date and time:", formatted_now)

# 2. Calculating the Difference Between Two Dates
current_time = datetime.now()
new_years_eve = datetime(current_time.year, 12, 31)
if current_time > new_years_eve:
    new_years_eve = datetime(current_time.year + 1, 12, 31)
days_remained = new_years_eve - current_time
print("Days remained for New Year's Eve:", days_remained.days)

# 3. Implementing a Countdown Timer
def countdown_timer(seconds):
    ending_time = datetime.now() + timedelta(seconds=seconds)
    while True:
        remaining = ending_time - datetime.now()
        total_seconds = int(remaining.total_seconds())

        if total_seconds <= 0:
            print("Time's up!")
            break

        print(f"Time remaining: {total_seconds} seconds", end="\r")
        time.sleep(1)
    print("\nTimer finished!")

countdown_timer(1)

# 4. Creating a Simple Month Calendar
def simple_calendar(year, month):
    current_date = datetime(year, month, 1)
    start_weekday = current_date.weekday()
    if month == 12:
        next_month = datetime(year + 1, 1, 1)
    else: next_month = datetime(year, month + 1, 1)
    last_date = next_month - timedelta(days=1)

    print("Mon Tue Wed Thu Fri Sat Sun")
    print("    " * start_weekday, end="")

    while current_date <= last_date:
        print(f"{current_date.day:3}", end="")
        if current_date.weekday() == 6:
            print()
        current_date += timedelta(days=1)
    print()

simple_calendar(2026, 2)