import time
import calendar

ticks = time.time()
print("Time is: ", ticks)

current_time = time.localtime(time.time())
print("Current time is: ", current_time)

localtime = time.asctime(time.localtime(time.time()))
print("Local time is: ", localtime)

print(calendar.isleap(2020))

calendar = calendar.month(2021, 10, width= 2, line= 1)
print("Calendar is: ", calendar)

