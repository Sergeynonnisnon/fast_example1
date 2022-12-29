import os, psutil
import time

while True:
    process = psutil.Process(os.getpid())
    t = time.time()
    for _ in range(100000):
        a = [process.memory_info().rss, process.cpu_percent(), process.username(), process.connections()]
    print(time.time() - t)
