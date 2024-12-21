# Day 3

## Part 1

Add all of the results of the multiplication instructions

Use regex to extract the instructions out

Regex pattern: `mul\(\d+,\d+\)`

- `\d+`: Any number of digits [0..9]

I passed each instruction parsed into this function:

```python
def runOps(ops: str) -> int:
    # I am not proud of this
    ew = ops[4:-1].split(',')
    return int(ew[0]) * int(ew[1])
```

## Part 2

I learned about the `|` operator

`do\\(\\)|don't\\(\\)|mul\\(\\d+,\\d+\\)`

Applied the same idea as part 1 but I added a condition to call the `runOps()` on certain instructions.

```python
for op in ops:
    if op == "don't()":
        do = False
        continue
    elif op == 'do()':
        do = True
        continue
    if do:
        sum += runOps(op)
```
