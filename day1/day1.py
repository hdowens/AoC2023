from time import perf_counter

def word2num(input: str) -> str:
    #words wrap , e.g. eightwothree
    #needs to be translated to 823
    #problem is, as the code iterates over the dict it would be translated as so:
    #eigh2three
    #eigh23
    #^so we need the last and first letter of each word for this to be 
    #a correct solution, hence the dict below
    num_dict = {
        'zero'  : '0',
        'one'   : 'o1e',
        'two'   : 't2o',
        'three' : 't3e',
        'four'  : 'f4r',
        'five'  : 'f5e',
        'six'   : 's6x',
        'seven' : 's7n',
        'eight' : 'e8t',
        'nine'  : 'n9e'
    }

    for item in num_dict:
        if item in input:
            #strings are immutable... gr
            input = input.replace(item, num_dict[item])
    return input

def main():

    with open("b:\Programming\Projects\AoC2023\day1\day1.txt" , "r") as puz_input:
        data = puz_input.readlines()

    ans = 0
    for string in data:
        #need to convert string to string w digits now
        string = word2num(string) #- UNCOMMENT THIS LINE FOR PART 2
        dig_list = [(i, c) for i, c in enumerate(string) if c.isdigit()]
        ans += int(dig_list[0][1] + dig_list[len(dig_list)-1][1])

    return ans
if __name__ == "__main__":
    st = perf_counter()
    print(f"Answer is: {main()}")
    end = perf_counter() - st
    print(f"Script completed in {end} seconds")