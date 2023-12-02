import math
from time import perf_counter
from collections import defaultdict

def part1(data: list) -> int:

    #we need to parse the data, and check at any time if the num pulled out
    #of red >12, green >13, blue >14

    rules = {
        "r" : 12,
        "g" : 13,
        "b" : 14
    }

    ans = 0
    for idx, game in enumerate(data):
        game_num = idx + 1
        turns = game.split(':')[1].split(";")
        
        violated = any(
            any(
                int(''.join(filter(str.isdigit, item))) > rules[item[item.find(next(filter(str.isalpha, item)))]] 
                for item in turn.split(",")
            )
            for turn in turns
        )

        if not violated:
            ans += game_num
    return ans

def part2(data: list) -> int:
    ans = 0
    for game in data:
        #use default dict to ignore setting it up + key errors
        maxs = defaultdict(int)
        turns = game.split(':')[1].split(";")

        for turn in turns:
            for item in turn.split(","):
                num = int(''.join(filter(str.isdigit, item)))
                col = item[item.find(next(filter(str.isalpha, item)))]
                maxs[col] = max(maxs[col], num)

        ans += math.prod(maxs.values())
            
    return ans

def main():

    with open("b:\Programming\Projects\AoC2023\day2\day2.txt" , "r") as puz_input:
        data = puz_input.readlines()

    #---------------------
    #someone elses soln, some people are cracked
    #---------------------
    #def f(line):
    #    bag = collections.defaultdict(int)
    #    for num, col in re.findall(r'(\d+) (\w+)', line):
    #        bag[col] = max(bag[col], int(num))
    #    return math.prod(bag.values())
#
    #print(sum(f(line) for line in data))


    p1_ans = part1(data)
    p2_ans = part2(data)

    return p1_ans, p2_ans
if __name__ == "__main__":
    st = perf_counter()
    print(f"Answer is: {main()}")
    end = perf_counter() - st
    print(f"Script completed in {end} seconds")

