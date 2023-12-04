import re
from time import perf_counter

def main():

    with open("b:\Programming\Projects\AoC2023\day3\day3.txt" , "r") as puz_input:
        data = puz_input.readlines()


    #data = [
    #    "........265............905..64.&...589..960..................*.......*..........62..19.........152................*.......+.....243......962",
    #    "...........*..220......*.......757.#..............-270..697..588....461..263......*.......@373....*........464...244...688..............*...",
    #    ".........272..........993.536..............................*............&......961....=..........490..198.....*................181.....236..",
    #]
#
    #data = [
    #    "12.......*..",
    #    "+.........34",
    #    ".......-12..",
    #    "..78........",
    #    "..*....60...",
    #    "78.........9",
    #    ".5.....23..$",
    #    "8...90*12...",
    #    "............",
    #    "2.2......12.",
    #    ".*.........*",
    #    "1.1..503+.56",
    #]

    #data = [
    #    ".......5......",
    #    "..7*..*.......",
    #    "...*13*.......",
    #    ".......15.....",
    #]


    ans = 0
    p2_ans = 0

    #I have no good ideas atm, going to brute force the fuck out of this
    atrks = {}

    for idx, item in enumerate(data):
        item = item.strip()
        for ma in re.finditer(r'\d+', item):

            for i in range(max(idx-1, 0), min(idx+2, len(data))):
                for j in range( max(ma.start()-1, 0), min(ma.end()+1, len(item))):

                    if not data[i][j].isdigit() and data[i][j] != '.':
                        ans += int(ma.group())

                    if data[i][j] == "*":
                        try:
                            num =  atrks[(i,j)]
                            p2_ans += (int(num) * int(ma.group()))
                        except KeyError:
                            atrks[(i,j)] = ma.group()
                       


                        
                              
    return ans, p2_ans

if __name__ == "__main__":
    st = perf_counter()
    print(f"Answer is: {main()}")
    end = perf_counter() - st
    #print(f"Script completed in {end} seconds")
