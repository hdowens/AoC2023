import re

from math import sqrt
from time import perf_counter

test_data = [
    "Time:      7  15   30",
    "Distance:  9  40  200",
]

data = [
    "Time:        60     94     78     82",
    "Distance:   475   2138   1015   1650",
]


def calc_margin(t: int, d: int) -> int:
    d += 1e-6
    low  = (t - sqrt(t**2 - 4*d))//2
    high = (t + sqrt(t**2 - 4*d))//2
    return int(high-low)
   

def solve(data: list, p2: bool) -> int:
    if p2:
        data[0] = data[0].replace(" ", "")
        data[1] = data[1].replace(" ", "")

    nums  = list(map(int,re.findall(r'\d+', data[0])))
    times = list(map(int,re.findall(r'\d+', data[1])))
    num_races = len(nums)
    ans = 1
    for i in range(num_races):
        ans *= calc_margin(nums[i], times[i])

    return ans

def main():
    return solve(data, False), solve(data, True)


if __name__ == "__main__":
    st = perf_counter()
    print(f"Answer is => {main()}")
    print(f"Execution took => {perf_counter() - st}")