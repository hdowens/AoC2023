from time import perf_counter

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
    for idx, game in enumerate(data):
        maxs = {
            "r" : 0,
            "g" : 0,
            "b" : 0
        }
        turns = game.split(':')[1].split(";")
        #each turn we need to check if the condition has been violated
        #will use a flag for now, probs better way to do it though
        for turn in turns:
            for item in turn.split(","):
                num = int(''.join(filter(str.isdigit, item)))
                col = item[item.find(next(filter(str.isalpha, item)))]
                if num > maxs[col]:
                    maxs[col] = num

        ans += (maxs['r']*maxs['g']*maxs['b'])
            
    return ans

def main():

    with open("b:\Programming\Projects\AoC2023\day2\day2.txt" , "r") as puz_input:
        data = puz_input.readlines()

    p1_ans = part1(data)
    p2_ans = part2(data)

    return p1_ans, p2_ans
if __name__ == "__main__":
    st = perf_counter()
    print(f"Answer is: {main()}")
    end = perf_counter() - st
    print(f"Script completed in {end} seconds")

