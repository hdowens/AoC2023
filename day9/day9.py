test_input = """ 
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

def solve_part1(puz_input: str) -> int:

    tot = 0
    nums = puz_input.strip().split("\n")
    for sequence in nums:
        seq = [int(n) for n in sequence.split()]
        to_extrap = []
        while len(set(seq)) != 0:
            to_extrap.append(seq[-1])
            seq = [seq[i+1] - seq[i] for i in range(0, len(seq)-1)]

        tot += sum(to_extrap)

    return tot

def solve_part2(puz_input: str) -> int:
    tot = 0
    nums = puz_input.strip().split("\n")
    for sequence in nums:
        seq = [int(n) for n in sequence.split()]
        to_extrap = []
        while set(seq) != set([0]):
            to_extrap.append(seq[0])
            seq = [seq[i+1] - seq[i] for i in range(0, len(seq)-1)]

        for i in range(len(to_extrap)-1, 0, -1):
            #lil bitta dynamic programming spoice - you love to see it
            to_extrap[i-1] = to_extrap[i-1] - to_extrap[i]

        #as the summation happens rhs to lhs, the final answer will be on the very lhs value,
        #the first value in the list!
        tot += to_extrap[0]

    return tot


def main():

    with open("b:\Programming\Projects\AoC2023\day9\day9.txt", "r") as f:
       puz_input = f.read()
    
    print(f"Answer to part 1 => {solve_part1(puz_input)}")
    print(f"Answer to part 2 => {solve_part2(puz_input)}")

if __name__ == "__main__":
    main()

