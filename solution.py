def find_incidents_timing(n: int, k: int, capacities: list[int]) -> tuple[int, int]:
    __input_sanity_check(n, k, capacities)

    return (__last_tank_overflowing_time(n, k, capacities), __all_tanks_full_time(n, k, capacities))

def __input_sanity_check(n: int, k: int, capacities: list[int]):
    if not (1 <= n <= 10**5):
        raise ValueError(f"n must be between 1 and 100000 (got {n})")
    if not (1 <= k <= 10**5):
        raise ValueError(f"k must be between 1 and 100000 (got {k})")
    if len(capacities) != n:
        raise ValueError(f"Expected {n} capacities, got {len(capacities)}")
    for i, c in enumerate(capacities, 1):
        if not (1 <= c <= 10**9):
            raise ValueError(f"capacity[{i}]={c} out of range [1, 1e9]")

def __last_tank_overflowing_time(n: int, k: int, capacities: list[int]) -> int:
    sum_from_the_end = 0
    best_numerator = None
    best_denominator = None

    for l in range(1, n+1):
        sum_from_the_end += capacities[-l]
        numerator = sum_from_the_end
        denominator = l*k

        if best_numerator is None or numerator * best_denominator < best_numerator * denominator:
            best_numerator, best_denominator = numerator, denominator
    
    return best_numerator // best_denominator

def __all_tanks_full_time(n: int, k: int, capacities: list[int]) -> int:
    sum_from_the_start = 0
    best_numerator = 0
    best_denominator = 1

    for i in range(1, n+1):
        sum_from_the_start += capacities[i-1]
        numerator = sum_from_the_start
        denominator = i*k

        if numerator * best_denominator > best_numerator * denominator:
            best_numerator, best_denominator = numerator, denominator

    return best_numerator // best_denominator
