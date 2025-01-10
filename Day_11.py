from datetime import datetime
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
current_hour = int(time.strftime('%H'))
if (12 <= current_hour < 16):
    print("Good afternoon")
elif (16 <= current_hour < 20):
    print("Good Evening")
elif (current_hour < 12):
    print("Good Morning")
else:
    print("Good Night")
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
