from time import perf_counter
from collections import Counter

VALUES    = dict(zip('23456789TJQKA', range(13)))
VALUES_P2 = dict(zip('J23456789TQKA', range(13)))

def hand2score(cards: str, p2: bool) -> int:
    cou = Counter(cards)
   
    if p2 and "J" in cards:
        jc = cou["J"]
        del cou["J"]
        #if it wsa all just J's, replace with best hand possible
        if len(cou) == 0:
            cou["A"] = 5
        #else replace the best hand with the amount of Js
        else:
            mc, _ = cou.most_common()[0]
            cou[mc] += jc

    #1. check for five of a kind
    if max(cou.values()) == 5:
        return 7
    #2. 4 of a kind
    elif max(cou.values()) == 4:
        return 6
    #3. fullhouse
    elif len(cou) == 2 and max(cou.values()) == 3:
        return 5
   
    #3. 3 of a kind
    elif max(cou.values()) == 3:
        return 4

    #4. twopair
    elif len(cou) == 3 and max(cou.values()) == 2:
        return 3

    #5. onepair
    elif len(cou) == 4 and max(cou.values()) == 2:
        return 2
   
    #6.highcard
    else:
        return 1

def line2score(line) -> list:
    return [hand2score(line[0], False)] + [VALUES[c] for c in line[0]]

def line2scorep2(line) -> list:
    return [hand2score(line[0], True)] + [VALUES_P2[c] for c in line[0]]

def main():

    with open("day7.txt", "r") as input:
        data = input.read().splitlines()

    scores = [(card, int(bid)) for card, bid in (line.split() for line in data)]

    ordered_p1 = sorted(scores, key=lambda x: line2score(x))
    ans_p1 = sum(bid * (idx + 1) for idx, (_, bid) in enumerate(ordered_p1))

    ordered_p2 = sorted(scores, key=lambda x: line2scorep2(x))
    ans_p2 = sum(bid * (idx + 1) for idx, (_, bid) in enumerate(ordered_p2))
    return ans_p1, ans_p2
   
if __name__ == "__main__":
    st = perf_counter()
    print(f"Answer is => {main()}")
    print(f"Execution took => {perf_counter() - st}")