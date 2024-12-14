import re

def runOps(ops: str) -> int:
    # I am not proud of this
    ew = ops[4:-1].split(',')
    return int(ew[0]) * int(ew[1])

def part1(): 
    with open("./input.txt") as f:
        pattern = re.compile("mul\\(*\\d+,\\d+\\)")
        ops = re.findall(pattern, f.read())
        sum: int = 0
        for o in ops:
            sum += runOps(o)
        print(sum)

def part2():
    with open("./input.txt") as f:
        pattern = re.compile("")
    pass
