# Glowing and flowing

## Description
A radioactive waste disposal company has a system of `n` cascading tanks, that are constantly being filled with irradiated water with a fixed rate of flow. Specifically, all tanks have their own valve, and they simultaneously feed water into them, with a fixed rate of `k` units of water per second for each valve.

Each tank has a predefined integer capacity. Once the `i-th` tank overflows, it starts filling the `i+1-th` tank with its surplus flow as a safety measure. If the last tank overflows, its surplus will be spilled to the containment.

We're interested to find out timings of two incidents that can happen:
- The number of seconds until the last tank starts overflowing (1)
- The number of seconds until all tanks are completely full (2)

You can presume that we start at a time zero, and all tanks are empty at this point.

### Input
The first line contains integers `n` and `k` (the number of tanks, and their input flow respectively), `1 ≤ n ≤ 10^5` , `1 ≤ k ≤ 10^5`. The `i-th` of the following `n` lines contains the integer capacity `ci` of the `i-th` tank, `1 ≤ ci ≤ 10^9`.

### Output
Prints two space separated integers on a single line, stating the number of seconds until the last tank starts overflowing, and the number of seconds until all tanks are completely full, rounded down to whole seconds.

## Requirements
- Python 3.13 or higher
- Pytest (tests only)

## Run
Run the program using Python and redirect the input file into the script:
```
python solve.py < input.txt
```
