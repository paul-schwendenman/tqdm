import tqdm
import time

for _ in tqdm.tqdm(range(400), desc="fast"):
    time.sleep(.01)

for _ in tqdm.tqdm(range(4), 'slow'):
    time.sleep(1)

for _ in tqdm.tqdm((_ for _ in range(40)), desc='unknown'):
    time.sleep(0.1)

