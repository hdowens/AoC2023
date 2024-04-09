def adjacent_matches(row: list) -> list:
    potent = []
    for idx, value in enumerate(row):
        if idx == len(row) - 1:
            pass
        else:
            if value == row[idx+1]:
                potent.append(idx)
    return potent

def main() -> None:
    with open("b:/Programming/Projects/AoC2023/day13/day13.txt", "r") as f:
        puz_input = f.read()


    

def solve_part1(puz_input):
    tot = 0
    for mirror in puz_input.split("\n\n"):
        grid = mirror.splitlines()
        adj = adjacent_matches(grid)
        for adj in adj:
            #print(f"match found row-wise at positions {adj, adj+1} in grid: {idx+1}")
            bf = list(reversed(grid[:adj]))
            af = grid[adj+2:]

            #print(bf, af)
            length = min(len(bf), len(af))
            if bf[:length] == af[:length]:
                tot += (adj+1)*100
  

        grid = [*zip(*grid)]
        adj = adjacent_matches(grid)
        for adj in adj:
            #print(f"match found col-wise at positions {adj, adj+1} in grid: {idx+1}")
            bf = list(reversed(grid[:adj]))
            af = grid[adj+2:]


            length = min(len(bf), len(af))
            if bf[:length] == af[:length]:
                tot += (adj+1)


    print(f"Potential answer to part1 => {tot}")




if __name__ == "__main__":
    main()