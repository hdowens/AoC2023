import math
from time import perf_counter
from collections import defaultdict

def main():

    #with open("b:\Programming\Projects\AoC2023\day3\day3.txt" , "r") as puz_input:
    #    data = puz_input.readlines()

    data = [
        ".467.114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ]

    def get_whole_num(row: int, col: int, dir: str) -> int:
        pass

    ans = 0
    #I have no good ideas atm, going to brute force the fuck out of this
    for row_num, item in enumerate(data):
        for idx, char in enumerate(item):
            #special character check
            if not char.isdigit() and char != '.':
                #print(f"pos: {idx +1} char: {char} row num: {row_num}")
                
                #now need to check adjacents
                #lhs in the row
                if item[idx-1].isdigit():
                    num = []
                    i = 1
                    while idx-i >= 0 and item[idx-i].isdigit():
                        #print(f"Num adjacent to char {char}: {item[idx-i]}")
                        num.append(item[idx-i])
                        i += 1
                    ans += int(''.join(i for i in reversed(num)))

                ##rhs in the row
                if item[idx+1].isdigit():
                    num = []
                    i = 1
                    while idx+i < len(item) and item[idx+i].isdigit():
                        #print(f"Num adjacent to char {char}: {item[idx-i]}")
                        num.append(item[idx+i])
                        i += 1
                    ans += int(''.join(i for i in num))


                #up
                #fuck
                #found another edge case
                #...112...
                #....-....
                #need to read 112, so need to check everygthinfg1!
                #making a big assumption here... nums are only <=3 digits long

                if row_num > 0:
                    #directly above
                    if data[row_num-1][idx].isdigit():

                        #edge case first
                        if data[row_num-1][idx-1].isdigit() and data[row_num-1][idx+1].isdigit():
                            ans += int(data[row_num-1][idx-1] + data[row_num-1][idx] + data[row_num-1][idx+1])


                        #top left
                        elif data[row_num-1][idx-1].isdigit():
                            num = []
                            i = 0
                            while idx-i >= 0 and data[row_num-1][idx-i].isdigit():
                                #ans += int(f"Num adjacent to char {char}: {item[idx-i]}")
                                num.append(data[row_num-1][idx-i])
                                i += 1
                            ans += int(f"middle top left num:{''.join(i for i in reversed(num))}")
                        
                        #top right
                        elif data[row_num-1][idx+1].isdigit():
                            num = []
                            i = 0
                            while idx+i < len(item) and data[row_num-1][idx+i].isdigit():
                                #print(f"Num adjacent to char {char}: {item[idx-i]}")
                                num.append(data[row_num-1][idx+i])
                                i += 1
                            ans += int(f"middle top right num: {''.join(i for i in num)}")
                    
                    
                    #top left
                    elif data[row_num-1][idx-1].isdigit():
                        num = []
                        i = 1
                        while idx-i >= 0 and data[row_num-1][idx-i].isdigit():
                            #print(f"Num adjacent to char {char}: {item[idx-i]}")
                            num.append(data[row_num-1][idx-i])
                            i += 1
                        ans += int(f"top left num: {''.join(i for i in reversed(num))}")

                    #top right
                    elif data[row_num-1][idx+1].isdigit():
                        num = []
                        i = 1
                        while idx+i < len(item) and data[row_num-1][idx+i].isdigit():
                            #print(f"Num adjacent to char {char}: {item[idx-i]}")
                            num.append(data[row_num-1][idx+i])
                            i += 1
                        ans += int(f"top right num: {''.join(i for i in num)}")
                #down
                if row_num < len(data):
                    #directly below
                    if data[row_num+1][idx].isdigit():

                        #edge case first
                        if data[row_num+1][idx-1].isdigit() and data[row_num+1][idx+1].isdigit():
                            ans += int(data[row_num+1][idx-1] + data[row_num+1][idx] + data[row_num+1][idx+1])


                        #top left
                        elif data[row_num+1][idx-1].isdigit():
                            num = []
                            i = 0
                            while idx-i >= 0 and data[row_num+1][idx-i].isdigit():
                                #print(f"Num adjacent to char {char}: {item[idx-i]}")
                                num.append(data[row_num+1][idx-i])
                                i += 1
                            ans += int(f"middle bottom left num:{''.join(i for i in reversed(num))}")
                        
                        #top right
                        elif data[row_num+1][idx+1].isdigit():
                            num = []
                            i = 0
                            while idx+i < len(item) and data[row_num+1][idx+i].isdigit():
                                #print(f"Num adjacent to char {char}: {item[idx-i]}")
                                num.append(data[row_num+1][idx+i])
                                i += 1
                            ans += int(f"middle bottom right num: {''.join(i for i in num)}")
                    
                    
                    #top left
                    elif data[row_num+1][idx-1].isdigit():
                        num = []
                        i = 1
                        while idx-i >= 0 and data[row_num+1][idx-i].isdigit():
                            #print(f"Num adjacent to char {char}: {item[idx-i]}")
                            num.append(data[row_num+1][idx-i])
                            i += 1
                        ans += int(f"bottom left num: {''.join(i for i in reversed(num))}")

                    #top right
                    elif data[row_num+1][idx+1].isdigit():
                        num = []
                        i = 1
                        while idx+i < len(item) and data[row_num+1][idx+i].isdigit():
                            #print(f"Num adjacent to char {char}: {item[idx-i]}")
                            num.append(data[row_num+1][idx+i])
                            i += 1
                        ans += int(f"bottom right num: {''.join(i for i in num)}")

    return ans
if __name__ == "__main__":
    st = perf_counter()
    print(f"Answer is: {main()}")
    end = perf_counter() - st
    print(f"Script completed in {end} seconds")
