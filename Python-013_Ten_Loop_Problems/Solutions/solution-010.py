# QS.10. Exponential Backoff strategy

import time

wait_time = 1   # Initial wait time in seconds
max_retries = 5
attempts = 0

while attempts < max_retries:
    print(f"Attempt {attempts + 1} of {max_retries} and will wait for {wait_time} seconds")
    time.sleep(wait_time)
    attempts += 1
    wait_time *= 2
