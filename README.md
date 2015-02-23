tqdm
====

Instantly make your loops show a progress meter - just wrap any iterable
with "tqdm(iterable)", and you're done!

tqdm (read ta<i>qa</i>dum, تقدّم) means "progress" in Arabic.


Here's an example of what the output looks like:

```python
>>> import time
>>> import tqdm
>>> for _ in tqdm.tqdm(range(400), desc="fast"):
...     time.sleep(.01)
... 
fast: [****************************************] 400/400 100% [00:04, 00:00, 98.78 #/s]
>>> for _ in tqdm.tqdm(range(4), 'slow'):
...     time.sleep(1)
... 
slow: [****************************************] 4/4 100% [00:04, 00:00,  1.00 #/s]
>>> for _ in tqdm.tqdm((_ for _ in range(40)), desc='unknown'):
...     time.sleep(0.1)
... 
unknown: 40 [00:04,  9.98 #/s]
```

Here's the doc:

```python
def tqdm(iterable, desc='', total=None, leave=False, mininterval=0.5, miniters=1):
    """
    Get an iterable object, and return an iterator which acts exactly like
    the iterable, but prints a progress meter and updates it every time a
    value is requested.

    'desc' can contain a short string, describing the progress, that is
    added in the beginning of the line.

    'total' can give the number of expected iterations. If not given,
    len(iterable) is used if it is defined.

    If leave is False, tqdm deletes its traces from screen after it has
    finished iterating over all elements.

    If less than mininterval seconds or miniters iterations have passed
    since the last progress meter update, it is not updated again.
    """
```

Installation instructions:

pip install git+https://github.com/paul-schwendenman/tqdm.git
