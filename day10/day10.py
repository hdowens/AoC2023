from collections import deque

test_input = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

def find_start(grid: str):
    for r, row in enumerate(grid):
        for c, cur in enumerate(row):
            if cur == "S":
                return (r, c)

def solve_part1(grid: str) -> int:
    start = find_start(grid)
    seen = {start}
    q = deque([start])

    while q:
        row, col = q.popleft()
        cur = grid[row][col]

        if row > 0 and cur in "S|JL" and grid[row - 1][col] in "|7F" and (row - 1, col) not in seen:
            seen.add((row - 1, col))
            q.append((row - 1, col))
            
        if row < len(grid) - 1 and cur in "S|7F" and grid[row + 1][col] in "|JL" and (row + 1, col) not in seen:
            seen.add((row + 1, col))
            q.append((row + 1, col))

        if col > 0 and cur in "S-J7" and grid[row][col - 1] in "-LF" and (row, col - 1) not in seen:
            seen.add((row, col - 1))
            q.append((row, col - 1))

        if col < len(grid[row]) - 1 and cur in "S-LF" and grid[row][col + 1] in "-J7" and (row, col + 1) not in seen:
            seen.add((row, col + 1))
            q.append((row, col + 1))

    #seen contains the entire set of elements of points in the grid
    #a bfs has been implemented so the furthest away will be the direc
    #middle of the set, so the find the length of the path to it
    #it is len(items) // 2
    return len(seen) // 2

def solve_part2(grid: str) -> int:
    start = find_start(grid)
    seen = {start}
    q = deque([start])

    replacement = {"|", "-", "J", "L", "7", "F"}

    while q:
        row, col = q.popleft()
        cur = grid[row][col]

        if row > 0 and cur in "S|JL" and grid[row - 1][col] in "|7F" and (row - 1, col) not in seen:
            seen.add((row - 1, col))
            q.append((row - 1, col))
            if cur == "S":
                replacement &= set('|JL')
            
        if row < len(grid) - 1 and cur in "S|7F" and grid[row + 1][col] in "|JL" and (row + 1, col) not in seen:
            seen.add((row + 1, col))
            q.append((row + 1, col))
            if cur == "S":
                replacement &= set('|7F')

        if col > 0 and cur in "S-J7" and grid[row][col - 1] in "-LF" and (row, col - 1) not in seen:
            seen.add((row, col - 1))
            q.append((row, col - 1))
            if cur == "S":
                replacement &= set('-J7')
        if col < len(grid[row]) - 1 and cur in "S-LF" and grid[row][col + 1] in "-J7" and (row, col + 1) not in seen:
            seen.add((row, col + 1))
            q.append((row, col + 1))
            if cur == "S":
                replacement &= set('-LF')
                

    grid = [row.replace("S", list(replacement)[0]) for row in grid]
    grid = ["".join(ch if (r, c) in seen else "." for c, ch in enumerate(row)) for r, row in enumerate(grid)]

    outside = set()

    for r, row in enumerate(grid):
        within = False
        up = None
        for c, ch in enumerate(row):
            if ch == "|":
                assert up is None
                within = not within
            elif ch == "-":
                assert up is not None
            elif ch in "LF":
                assert up is None
                up = ch == "L"
            elif ch in "7J":
                assert up is not None
                if ch != ("J" if up else "7"):
                    within = not within
                up = None
            else:
                pass
           
            if not within:
                outside.add((r, c))
                
    #idea here is that we compute all the points which are 
    #1. in the path, what we did in part1
    #2. outside of the path
    #then its just the size of the grid - the number of these points (not including dups)
    
    return len(grid) * len(grid[0]) - len(outside | seen)


def main() -> None:

    with open("b:\Programming\Projects\AoC2023\day10\day10.txt", "r") as f:
       puz_input = f.read()
    
    grid = puz_input.strip().splitlines()
    print(solve_part1(grid))
    print(solve_part2(grid))
    
if __name__ == "__main__":
    main()