#!/usr/bin/env python3
import time

if __name__ == '__main__':
    while True:
        print(time.ctime(time.time()),flush=True)
        time.sleep(10)
