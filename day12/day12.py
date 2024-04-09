import re
from functools import cache

test_input_good = """#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1"""

test_input_broken = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def validate_springs(status: str, positions: str) -> bool:
    # Ensure positions are within the bounds of the status string
    if positions[0] > len(status):
        return False
    
    # Check if there are no "." characters before the specified position
    if "." in status[:positions[0]]:
        return False
    
    # Check if the character at the specified position is not "#"
    if positions[0] != len(status) and status[positions[0]] == "#":
        return False
    
    return True

#cache it to make use of memoisation
@cache
def calc_spring_combinations(status: str, positions: str) -> int:
    """Generate all spring combinations given a status

    Args:
        status (str): Spring status
        positions (str): String representing positions

    Returns:
        int: Number of valid combinations
    """
    # Base case: If no positions left, check if status has any broken springs
    if not positions:
        return 1 if "#" not in status else 0
    
    # Base case: If status is empty but positions are not, no valid combinations
    if not status:
        return 0
    
    total = 0
    # If current character is a dot or question mark, proceed to next character
    if status[0] in (".", "?"):
        total += calc_spring_combinations(status[1:], positions)
    
    # If current character is "#" or "?", validate the configuration
    if status[0] in ("#", "?"):
        if validate_springs(status, positions):
            total += calc_spring_combinations(status[positions[0] + 1:], positions[1:])
    
    return total  

def main() -> None:
    #springs = test_input_broken.split("\n")

    with open("b:\Programming\Projects\AoC2023\day12\day12.txt", "r") as f:
        puz_input = f.read()

    springs = puz_input.splitlines()

    p1_tot = p2_tot = 0
    for record in springs:
        status, positions = record.split()
        positions = tuple(map(int, positions.split(",")))
        
        #pt1
        combinations = calc_spring_combinations(status, positions)
        p1_tot += combinations
        
        #pt2. need to unfold
        status = "?".join([status] * 5)
        positions = positions * 5
        p2_tot += calc_spring_combinations(status,positions)

    print(f"Answer to part 1: {p1_tot}")
    print(f"Answer to part 2: {p2_tot}")

if __name__ == "__main__":
    main()