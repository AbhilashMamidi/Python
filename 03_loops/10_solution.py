
# 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles
#  the wait time between retries, starting from 1 second,
#  but stops after 5 retries.

import time

wait_time = 1
max_retrives = 5
attempts = 0

while attempts < max_retrives :
    print("Attempts", attempts + 1 , "- wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1

#     Ans:
# Attempts 1 - wait time 1
# Attempts 2 - wait time 2
# Attempts 3 - wait time 4
# Attempts 4 - wait time 8
# Attempts 5 - wait time 16
