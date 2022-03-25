from typing import List, Union
Num = Union[int, float]

class Hash:
    def __init__(self, cumsum: Num, start_idx: int, end_idx: int):
        self.cumsum = cumsum
        self.end_idx = end_idx
        self.start_idx = start_idx

class Cumsum:
    def __init__(self, data: List[List[Num]], window: Num):
        self.hash = {}
        self.data = data
        self.window = window
        self.bootstrap(data)

    def bootstrap(self, data: List[List[Num]]):
        i = 0
        if len(self.hash) == 0:
            dt, val = data[0]
            self.hash[dt] = Hash(val,0,0)
            i += 1
        while i < len(data):
            last_key = list(self.hash.keys())[-1]
            prev_hash = self.hash[last_key]
            start_idx = prev_hash.start_idx
            dt, val = data[i]
            cumsum = val + prev_hash.cumsum
            while dt - self.data[start_idx][0] > self.window:
                cumsum -= self.data[start_idx][1]
                start_idx += 1
            self.hash[dt] = Hash(cumsum, start_idx, i)
            i += 1
        return self.hash

    def add_data(self, arr: List[List[Num]]):
        self.data += arr
        self.bootstrap(arr)

    def __getitem__(self, dt: Num):
        if dt not in self.hash.keys():
            dt = max([k for k in list(self.hash.keys()) if k < dt])
        return (dt, self.hash[dt].cumsum)



# data = [[1.0,20], [2.0,0], \
#         [2.1,20], [3.0,203], [3.4, 120]]
# cs = CumSum(data)
# cs.hash
# [1.0: <object#hash cumsum: 20, start_idx: 0, end_idx: 0>,
#  2.0: <object#hash cumsum: 0, start_idx: 1, end_idx: 1>,
#  2.1: <object#hash cumsum: 20, start_idx: 1, end_idx: 2>,
#  3.0: <object#hash cumsum: 223, start_idx: 2, end_idx: 3>,
#  3.4: <object#hash cumsum: 323, start_idx: 3, end_idx: 4>]
# cs[2.1] = 20
# cs.add_data([[3.5, 102], [3.6, 12], [3.8, 120]])
