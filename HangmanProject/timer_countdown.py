import time
import datetime
import random
 

def expert_mode():
    total_seconds = 90
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("Times up!!!! The countdown is at zero seconds!")
 
