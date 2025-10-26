def find_incidents_timing(n: int, k: int, capacities: list[int]) -> tuple[int, int]:
    """
    Compute both key incident timings for a cascading tank system.

    This function returns:
      1) The time (in seconds, floored) until the last tank starts overflowing
         to the containment.
      2) The time (in seconds, floored) until all tanks are completely full.

    The system model:
      - Each tank receives an independent inflow of `k` units of water per second.
      - If a tank overflows, the surplus water flows into the next tank.
      - The last tank's overflow is lost to the containment.
      - All tanks are initially empty at time zero.

    Args:
        n: Number of tanks (1 <= n <= 10^5).
        k: Inflow rate per tank (1 <= k <= 10^5).
        capacities: List of tank capacities (each 1 <= c_i <= 10^9).

    Returns:
        A tuple (t_spill, t_full) where:
          - t_spill: Time until the last tank starts overflowing.
          - t_full:  Time until all tanks are full.

    Raises:
        ValueError: If any input value is outside the allowed range.
    """
    __input_sanity_check(n, k, capacities)
    return (
        __last_tank_overflowing_time(n, k, capacities), 
        __all_tanks_full_time(n, k, capacities)
    )

def __input_sanity_check(n: int, k: int, capacities: list[int]):
    """
    Validate input parameters for the tank simulation.

    Ensures all numeric parameters are within problem constraints and that
    the number of capacity values matches the declared number of tanks.

    Args:
        n: Number of tanks.
        k: Inflow rate per tank.
        capacities: List of tank capacities.

    Raises:
        ValueError: If n, k, or any capacity is outside its valid range.
    """
    if not (1 <= n <= 10**5):
        raise ValueError(f"n={n} is out of range [1, 10^5]")
    if not (1 <= k <= 10**5):
        raise ValueError(f"k={k} is out of range [1, 10^5]")
    if len(capacities) != n:
        raise ValueError(f"Expected {n} capacities, got {len(capacities)}")
    for i, c in enumerate(capacities, 1):
        if not (1 <= c <= 10**9):
            raise ValueError(f"capacity[{i}]={c} out of range [1, 10^9]")

def __last_tank_overflowing_time(n: int, k: int, capacities: list[int]) -> int:
    """
    Calculate the time until the last tank starts overflowing.

    For each continuous subset of l tanks (counting from the last tank),
    compute the average filling time for that subset:
        time_l = (sum of last l capacities) / (l * k)
    The earliest possible overflow time for the last tank is the minimum
    of all such averages.

    Args:
        n: Number of tanks.
        k: Inflow rate per tank.
        capacities: List of tank capacities.

    Returns:
        The floored time (in seconds) when the last tank first overflows.

    Complexity:
        Time: O(n)
        Additional memory: O(1)
    """
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
    """
    Calculate the time until all tanks are completely full.

    For each continuous subset of i tanks (starting from the first tank),
    compute the average filling time:
        time_i = (sum of first i capacities) / (i * k)
    The system is entirely full when every subset can hold all the water
    it has received, i.e., when t >= max(time_i).

    Args:
        n: Number of tanks.
        k: Inflow rate per tank.
        capacities: List of tank capacities.

    Returns:
        The floored time (in seconds) when all tanks are full.

    Complexity:
        Time: O(n)
        Additional memory: O(1)
    """
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
