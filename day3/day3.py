from time import perf_counter

def main():

    with open("b:\Programming\Projects\AoC2023\day3\day3.txt" , "r") as puz_input:
        data = puz_input.readlines()


    #data = [
    #    "........265............905..64.&...589..960..................*.......*..........62..19.........152................*.......+.....243......962",
    #    "...........*..220......*.......757.#..............-270..697..588....461..263......*.......@373....*........464...244...688..............*...",
    #    ".........272..........993.536..............................*............&......961....=..........490..198.....*................181.....236..",
    #]

    ans = 0

    #I have no good ideas atm, going to brute force the fuck out of this
    for row_num, item in enumerate(data):
        item = item.strip()
        for idx, char in enumerate(item):
            
            #special character check
            if not char.isdigit() and char != '.':
                #print(f"pos: {idx +1} char: {char} row num: {row_num}")
                #now need to check adjacents
                #lhs in the row
                if idx-1 >= 0 and item[idx-1].isdigit():
                    num = []
                    i = 1
                    while idx-i >= 0 and item[idx-i].isdigit():    
                        num.append(item[idx-i])
                        i += 1
                    ans += int(''.join(i for i in reversed(num)))


                ##rhs in the row
                if idx+1 < len(item) and item[idx+1].isdigit():
                    num = []
                    i = 1
                    while idx+i < len(item) and item[idx+i].isdigit():
                        num.append(item[idx+i])
                        i += 1
                    ans += int(''.join(i for i in num))


                #up
                if row_num > 0:


                    #directly above
                    if data[row_num-1][idx].isdigit():

                        #edge case first
                        if data[row_num-1][idx-1].isdigit() and data[row_num-1][idx+1].isdigit():
                            toadd = str(data[row_num-1][idx-1]) + str(data[row_num-1][idx]) + str(data[row_num-1][idx+1])
                            ans += int(toadd)
                            print(f"{data[row_num-1][idx-1] + data[row_num-1][idx] + data[row_num-1][idx+1]}")

                        else:

                            #if its just a single digit above rhs col
                            if idx+1 == len(item) and data[row_num-1][idx-1] == '.':
                                ans += int(data[row_num-1][idx])
                                print(f"{data[row_num-1][idx]}")


                            #if its just a single digit above lhs col
                            if idx+1 == 1 and data[row_num-1][idx+1] == '.':
                                ans += int(data[row_num-1][idx])
                                print(f"{data[row_num-1][idx]}")


                            #top left
                            if data[row_num-1][idx-1].isdigit():
                                num = []
                                i = 0
                                while idx-i >= 0 and data[row_num-1][idx-i].isdigit():
                                    #ans += int(f"Num adjacent to char {char}: {item[idx-i]}")
                                    num.append(int(data[row_num-1][idx-i]))
                                    i += 1
                                ans += int(''.join(str(i for i in reversed(num)))

                            
                            #top right
                            if idx+i < len(item) and data[row_num-1][idx+1].isdigit():
                                num = []
                                i = 0
                                while idx+i < len(item) and data[row_num-1][idx+i].isdigit():
                                    #print(f"Num adjacent to char {char}: {item[idx-i]}")
                                    num.append(int(data[row_num-1][idx+i]))
                                    i += 1
                                ans += int(''.join(str(i) for i in num))

                    
                    
                    #top left
                    else:
                        if data[row_num-1][idx-1].isdigit():
                            num = []
                            i = 1
                            while idx-i >= 0 and data[row_num-1][idx-i].isdigit():
                                #print(f"Num adjacent to char {char}: {item[idx-i]}")
                                num.append(int(data[row_num-1][idx-i]))
                                i += 1
                            ans += int(''.join(str(i) for i in reversed(num)))


                        #top right
                        if idx+1 < len(item) and data[row_num-1][idx+1].isdigit():
                            num = []
                            i = 1
                            while idx+i < len(item) and data[row_num-1][idx+i].isdigit():
                                #print(f"Num adjacent to char {char}: {item[idx-i]}")
                                num.append(int(data[row_num-1][idx+i]))
                                i += 1
                            ans += int(''.join(str(i) for i in num))

                
                #down
                if row_num+1 < len(data):
                    #directly below
                    if data[row_num+1][idx].isdigit():

                        #edge case first
                        if idx-1 >= 0 and data[row_num+1][idx-1].isdigit() and  idx+i < len(item) and data[row_num+1][idx+1].isdigit():
                            toadd = str(data[row_num+1][idx-1]) + str(data[row_num+1][idx]) + str(data[row_num+1][idx+1])
                            ans += int(toadd)
                            print(f"{data[row_num+1][idx-1] + data[row_num+1][idx] + data[row_num+1][idx+1]}")


                        else:
                        

                            #if its just a single digit above in the rhs pos
                            if idx+1 == len(item) and data[row_num+1][idx-1] == '.':
                                ans += int(data[row_num+1][idx])
                                print(f"{data[row_num+1][idx]}")


                                                    #if its just a single digit above in the rhs pos
                            if idx+1 == 1 and data[row_num+1][idx+1] == '.':
                                ans += int(data[row_num+1][idx])
                                print(f"{data[row_num+1][idx]}")


                            #top left
                            if data[row_num+1][idx-1].isdigit():
                                num = []
                                i = 0
                                while idx-i >= 0 and data[row_num+1][idx-i].isdigit():
                                    #print(f"Num adjacent to char {char}: {item[idx-i]}")
                                    num.append(data[row_num+1][idx-i])
                                    i += 1
                                ans += int(''.join(i for i in reversed(num)))

                            
                            #top right
                            if data[row_num+1][idx+1].isdigit():
                                num = []
                                i = 0
                                while idx+i < len(item) and data[row_num+1][idx+i].isdigit():
                                    #print(f"Num adjacent to char {char}: {item[idx-i]}")
                                    num.append(int(data[row_num+1][idx+i]))
                                    i += 1
                                ans += int(''.join(str(i) for i in num))
    
                                
                    
                    else:
                        #top left
                        if data[row_num+1][idx-1].isdigit():
                            num = []
                            i = 1
                            while idx-i >= 0 and data[row_num+1][idx-i].isdigit():
                                #print(f"Num adjacent to char {char}: {item[idx-i]}")
                                num.append(int(data[row_num+1][idx-i]))
                                i += 1
                            ans += int(''.join(str(i) for i in reversed(num)))
 

                        #top right
                        if idx+1 < len(item) and data[row_num+1][idx+1].isdigit():
                            num = []
                            i = 1
                            while idx+i < len(item) and data[row_num+1][idx+i].isdigit():
                                #print(f"Num adjacent to char {char}: {item[idx-i]}")
                                num.append(int(data[row_num+1][idx+i]))
                                i += 1
                            ans += int(''.join(str(i) for i in num))


    return ans

if __name__ == "__main__":
    st = perf_counter()
    print(f"Answer is: {main()}")
    end = perf_counter() - st
    #print(f"Script completed in {end} seconds")
