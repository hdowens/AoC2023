from functools import reduce

seeds, *mappings = open('day5.txt').read().split('\n\n')
seeds = map(int, seeds.split()[1:])

print(mappings)

def lookup(start, mapping):
    for m in mapping.split('\n')[1:]:
        dst, src, len = map(int, m.split())
        delta = start - src
        if delta in range(len):
            return dst + delta
    else: return start

print(min(reduce(lookup, mappings, int(s)) for s in seeds))