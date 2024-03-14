test_input = """
    seeds: 79 14 55 13

    seed-to-soil map:
    50 98 2
    52 50 48

    soil-to-fertilizer map:
    0 15 37
    37 52 2
    39 0 15

    fertilizer-to-water map:
    49 53 8
    0 11 42
    42 0 7
    57 7 4

    water-to-light map:
    88 18 7
    18 25 70

    light-to-temperature map:
    45 77 23
    81 45 19
    68 64 13

    temperature-to-humidity map:
    0 69 1
    1 0 69

    humidity-to-location map:
    60 56 37
    56 93 4
    """


import re
from timer import time_that_bitch

@time_that_bitch
def solve_part1(puz_input: str) -> int:
    segments = puz_input.split('\n\n')
    seeds = re.findall(r'\d+', segments[0])
    cur_nums = [int(i) for i in seeds]
    for seg in segments[1:]:
        tmp = []
        maps = re.findall(r'\d+', seg)
        mappings = list(zip(*(iter(maps),) * 3))
        for num in cur_nums:
            curr_num_mapped = False

            for mp in mappings:
                #print(f"Source: {mp[1]}, Range: {mp[2]}, Destination:{mp[0]}")
                #print(f"Bounds to check: {mp[1]}-{int(mp[1]) + int(mp[2]) - 1}")
                if num <= int(mp[1]) + int(mp[2]) - 1 and num >= int(mp[1]):
                    tmp.append(int(mp[0]) + (num - int(mp[1])))
                    curr_num_mapped = True

            if not curr_num_mapped:
                tmp.append(num)
           
        cur_nums = tmp

    return min(cur_nums)

@time_that_bitch
def solve_part2(puz_input: str) -> int:
    segments = puz_input.split('\n\n')
    seeds = segments[0]

    intervals = []
    for se_int in re.findall(r'(\d+) (\d+)', seeds):
        lb, delta = map(int, se_int)
        ub = lb + delta
        #1 here is saying that these are all from the first mapping 
        #seed-to-soil, if you will
        intervals.append((lb, ub, 1))

    min_loc = float('inf')
    while intervals:
        lb, ub, idx = intervals.pop()

        #if we are at the end find the most min
        if idx == len(segments):
            min_loc = min(min_loc, lb)
            continue

        #map the ranges
        for conv in re.findall(r'(\d+) (\d+) (\d+)', segments[idx]):
            dest, src, delta = map(int, conv)
            end = src + delta
            diff = dest - src
            #no overlap
            if ub <= src or end <= lb:
                continue
            #overlap around the lower bound so split up
            if lb < src:
                intervals.append((lb, src, idx))
                lb = src

            #overlap around the upper bound so split up
            if ub > end:
                intervals.append((end, ub, idx))
                ub = end

            #entire overlap
            intervals.append((lb+diff, ub+diff, idx+1))
            break

        else:
            intervals.append((lb, ub, idx+1))

    return min_loc



def main():
    with open("b:\Programming\Projects\AoC2023\day5\day5.txt", "r") as f:
        puz_input = f.read()

    print(f"Answer to part 1 => {solve_part1(puz_input)}")
    print(f"Answer to part 2 => {solve_part2(puz_input)}")


if __name__ == "__main__":
    main()