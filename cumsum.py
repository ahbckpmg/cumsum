from typing import List, Union
Num = Union[int, float]

class Hash:
    def __init__(self, cumsum: Num, start_idx: int, end_idx: int):
        self.cumsum = cumsum
        self.end_idx = end_idx
        self.start_idx = start_idx

class OrderError(Exception):
    """Custom error for Cumsum"""

class Cumsum:
    """
    Calculates the cumulative sum for a given numeric datetime
    Each entry in the hash attribute is a Hash object
    The cumulative sum can be retrieved like getting an item and
    returns the index closest to the one entered
    Data is expected to be ordered in increasing order

    >>> data = [[1.0,20], [2.0,0], \
            [2.1,20], [3.0,203], [3.4, 120]]
    >>> cs = Cumsum(data)
    >>> cs[2.1]
    (2.1, 20)
    >>> cs.add_data([[3.5, 102], [3.6, 12], [3.8, 120]])
    >>> cs[3.9]
    (3.8, 557)
    """
    def __init__(self, data: List[List[Num]], window: Num):
        self.hash = {}
        self.data = data
        self.window = window
        self.bootstrap(data)

    def bootstrap(self, data: List[List[Num]]):
        i = 0
        last_key = ''
        if len(self.hash) == 0:
            dt, val = data[0]
            self.hash[dt] = Hash(val,0,0)
            last_key = dt
            i += 1
        while i < len(data):
            if last_key == '':
                last_key = list(self.hash.keys())[-1]
            prev_hash = self.hash[last_key]
            start_idx = prev_hash.start_idx
            dt, val = data[i]
            if last_key > dt:
                msg = 'Input data must be increasing in datetime\n'
                msg += f'{last_key} must be less than {dt}'
                raise OrderError(msg)
            cumsum = val + prev_hash.cumsum
            while dt - self.data[start_idx][0] > self.window:
                cumsum -= self.data[start_idx][1]
                start_idx += 1
            self.hash[dt] = Hash(cumsum, start_idx, i)
            last_key = dt
            i += 1
        return self.hash

    def add_data(self, arr: List[List[Num]]):
        self.data += arr
        self.bootstrap(arr)

    def __getitem__(self, dt: Num):
        if dt not in self.hash.keys():
            dt = max([k for k in list(self.hash.keys()) if k < dt])
        return (dt, self.hash[dt].cumsum)

