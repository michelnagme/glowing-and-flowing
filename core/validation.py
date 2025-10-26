def validate_input(n_raw: str, k_raw: str, capacities_raw: list[str]) -> tuple[int, int, list[int]]:
    errors: list[str] = []

    n = k = None
    try:
        n = int(n_raw)
    except Exception:
        errors.append(f"n must be an integer (got {n_raw!r})")
    try:
        k = int(k_raw)
    except Exception:
        errors.append(f"k must be an integer (got {k_raw!r})")

    if isinstance(n, int) and not (1 <= n <= 10**5):
        errors.append(f"n={n} is out of range [1, 10^5]")
    if isinstance(k, int) and not (1 <= k <= 10**5):
        errors.append(f"k={k} is out of range [1, 10^5]")

    if isinstance(n, int):
        if len(capacities_raw) != n:
            errors.append(f"Expected {n} capacities, got {len(capacities_raw)}")

    capacities: list[int] = []
    for idx, token in enumerate(capacities_raw):
        try:
            val = int(token)
        except Exception:
            errors.append(f"capacity[{idx}] must be an integer (got {token!r})")
            continue
        if not (1 <= val <= 10**9):
            errors.append(f"capacity[{idx}]={val} out of range [1, 10^9]")
        capacities.append(val)

    if errors:
        raise ValueError("Input validation failed:\n- " + "\n- ".join(errors))
    
    return n, k, capacities
