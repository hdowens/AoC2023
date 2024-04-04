import re
from typing import List
from itertools import combinations

test_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

def main() -> None:

    with open("b:\Programming\Projects\AoC2023\day11\day11.txt", "r") as f:
       puz_input = f.read()
       
    grid = puz_input.splitlines()
    
    #rows which are scaled
    row_add = []
    for cnt, row in enumerate(grid):
        if all(c == row[0] for c in row):
            row_add.append(cnt)
    
    #cols which are scaled
    col_add = []
    for i in range(len(grid[0])):
        col = [ele[i] for ele in grid]
        if all(c == col[0] for c in col):
            col_add.append(i)

    galaxies = set()
    for idx, row in enumerate(grid):
        pattern = re.compile(r'\#')
        for match in re.finditer(pattern, row):
            galaxies.add((idx, match.start()))

    #print(f"The number of pairs is: {len(galaxies) * (len(galaxies)-1) // 2}")=
    #print('\n'.join(i for i in grid))
    
    part1 = part2 = 0
    part1_scaler = 1
    part2_scaler = 1_000_000 - 1
    for a, b in combinations(galaxies, 2):
        #co-ords of our galaxies
        y1, x1, y2, x2 = a + b
        
        #compute how many rows and cols are crossed
        rows_crossed = set(row_add).intersection(range(min(y1, y2), max(y1, y2)))
        cols_crossed = set(col_add).intersection(range(min(x1, x2), max(x1, x2)))
        
        #compute manhattan distance and offset by the scaler!
        part1 += abs(x1 - x2) + abs(y1 - y2)
        part1 += (len(rows_crossed) * part1_scaler) + (len(cols_crossed) * part1_scaler) 
        
        part2 += abs(x1 - x2) + abs(y1 - y2)
        part2 += (len(rows_crossed) * part2_scaler) + (len(cols_crossed) * part2_scaler) 
        
    print(f"The solution to part 1 is: {part1}")
    print(f"The solution to part 2 is: {part2}")
   
    


if __name__ == "__main__":
    main()
    

#experimental & interesting code
#for i in range(0, len(grid)):
#    if all(c == grid[i][0] for c in grid[i]):
#        grid.insert(i, grid[i])
#(result, qty) = re.subn(r'\#', str(count), row)
#count += 1
#print(result, qty)       