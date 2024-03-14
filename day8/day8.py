test_input = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
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
        #print(f"{cur_place} mapping to {mapped_val} after going {[turns[i % len(turns)]]}")
        cur_place = mapped_val


def main():
    with open("b:\Programming\Projects\AoC2023\day8\day8.txt", "r") as f:
       puz_input = f.read()



    print(f"Answer to part 1 => {solve_part1(puz_input)}")
    #print(f"Answer to part 2 => {solve_part2(puz_input)}")


if __name__ == "__main__":
    main()