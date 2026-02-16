import math as m
radius = 5
area = m.pi * m.pow(radius, 2)
print(f"Area of circle: {area}")

import random
names = ["Alex", "Bob", "Nicolas"]
winner = random.choice(names)
print(f"Winner: {winner}")

from datetime import datetime, timedelta
now = datetime.now()
print(f"Current time: {now}")
future_date = now + timedelta(days=100)
print(f"Date after 100 days: {future_date}")