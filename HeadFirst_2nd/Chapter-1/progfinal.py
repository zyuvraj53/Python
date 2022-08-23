from datetime import date, datetime

import random
import time

odds = range(1, 60, 2)

while True:
  right_this_minute = datetime.today().minute
  if right_this_minute in odds:
    print("This minute seems a little odd.")
  else:
    print("Not an odd minute.")
  wait_timme = random.randint(1, 5)*0.1
  time.sleep(wait_timme)