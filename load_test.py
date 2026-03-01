# load_thread.py
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter
import time

URL = "http://localhost:8000/"
TOTAL = 5
MAX_WORKERS = 6   # concurrency cap (adjust)

counts = Counter()
errors = 0

def work(i):
    global errors
    try:
        r = requests.get(URL, timeout=10)
        data = r.json()
        pid = data.get("worker_pid")
        return pid
    except Exception as e:
        return f"ERR:{e}"

start = time.time()
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
    futures = [ex.submit(work, i) for i in range(TOTAL)]
    for f in as_completed(futures):
        res = f.result()
        if isinstance(res, int):
            counts[res] += 1
        else:
            counts[res] += 1

elapsed = time.time() - start
print(f"Elapsed: {elapsed:.2f}s")
print("Distribution:")
for k, v in counts.most_common():
    print(k, v)
