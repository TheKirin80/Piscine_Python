import time
import datetime

time_now = time.time()
print(f"Seconds since January 1, 1970: {time_now:,.4f} or {time_now:.2e} in scientific notation")
print(datetime.datetime.today().strftime('%b %d %Y'))