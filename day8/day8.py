from math import gcd
from functools import reduce

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


test_input = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

def solve_part1(puz_input: str) -> int:
    inp = puz_input.split("\n\n")
    turns = inp[0].strip()
    maps = {}
    directions = inp[1].strip()
    for row in directions.split("\n"):
        intra_map = {}
        dict_key = row.strip().split("=")[0].strip() 
        value = row.strip().split("=")[1].strip()
        lr = value.split(",")
        intra_map["L"] = lr[0][1:].strip()
        intra_map["R"] = lr[1][:-1].strip()
        maps[dict_key] = intra_map

    cur_place = "AAA"
    for i in range(0, 100_000):
        if cur_place == "ZZZ":
            #return number of steps
            return i
        mapped_val = maps[cur_place][turns[i % len(turns)]]
        cur_place = mapped_val

def solve_part2(puz_input: str) -> int:
    inp = puz_input.split("\n\n")
    turns = inp[0].strip()
    directions = inp[1].strip()

    active_states = []
    maps = {}
    for row in directions.split("\n"):
        intra_map = {}
        dict_key = row.strip().split("=")[0].strip()
        active_states.append(dict_key) if dict_key[2] == "A" else None 
        value = row.strip().split("=")[1].strip()
        lr = value.split(",")
        intra_map["L"] = lr[0][1:].strip()
        intra_map["R"] = lr[1][:-1].strip()
        maps[dict_key] = intra_map

    steps_needed = []
    i = 0
    while active_states:
        new_active_states = []
        for item in active_states:
            if item[-1] == "Z":
                steps_needed.append(i)     
            else:
                new_item = maps[item][turns[i % len(turns)]]
                new_active_states.append(new_item)
        i += 1
        active_states = new_active_states


    return reduce(lcm, steps_needed)

def main():
    with open("b:\Programming\Projects\AoC2023\day8\day8.txt", "r") as f:
       puz_input = f.read()
   
    print(f"Answer to part 1 => {solve_part1(puz_input)}")
    print(f"Answer to part 2 => {solve_part2(puz_input)}")
if __name__ == "__main__":
    main()






        #for i in range(0, 100_000):
    #    if all(t[2] == "Z" for t in active_states):
    #        print(f"we good after {i} steps")
    #        break
    #    tmp_list = []
    #    for item in active_states:
    #        mapped_val = maps[item][turns[i % len(turns)]]
    #    #print(f"{cur_place} mapping to {mapped_val} after going {[turns[i % len(turns)]]}")
    #        tmp_list.append(mapped_val)
    #    active_states = tmp_list