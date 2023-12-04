import re
from time import perf_counter
from collections import defaultdict

def main():

    #data = [
    #    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    #    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    #    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    #    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    #    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    #    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    #]

    with open("b:\Programming\Projects\AoC2023\day4\day4.txt" , "r") as puz_input:
        data = puz_input.readlines()

    part1_ans = 0
    card_count = {}

    for idx, row in enumerate(data):
        card_count[idx + 1] = 1

    for idx, row in enumerate(data):
        #1.get the winning nums into a list
        game_num = idx + 1 
        win_nums = re.findall(r'\d+', row.split(":")[1].split("|")[0])

        scratchy_nums = re.findall(r'\d+', row.split(":")[1].split("|")[1])
        

        #part 1
        part1_score = 0
        for item in scratchy_nums:
            if item in win_nums:
                if part1_score == 0:
                    part1_score += 1
                else:
                    part1_score *= 2
        part1_ans += part1_score

        #part 2
        for _ in range(card_count[game_num]):

            score = 0
            for item in scratchy_nums:
                if item in win_nums:
                    score += 1

            if score != 0:
                #print(f"Card {game_num} has #{score} numbers, so add {game_num+1}-{game_num+score} cards from this one")
                for i in range(game_num+1, game_num+score+1):
                    card_count[i] += 1

    return part1_ans, sum(card_count.values())
    

if __name__ == "__main__":
    st = perf_counter()
    print(f"Answer is: {main()}")
    end = perf_counter() - st
    print(f"Script completed in {end} seconds")

