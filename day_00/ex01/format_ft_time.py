import time
import datetime
import calendar

time_now = time.time()
print("Seconds since January 1, 1970:",format(round(time_now, 4),","),"or", "{:.2e}".format(time_now), "in scientific notation")
print(datetime.datetime.today().strftime('%b %d %Y'))