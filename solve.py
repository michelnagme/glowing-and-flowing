import sys
from core.validation import validate_input
from core.solution import find_incidents_timing


if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()

    if len(tokens) < 2:
        raise ValueError("Expected at least n and k")

    try:
        n, k, capacities = validate_input(tokens[0], tokens[1], tokens[2:])
    except ValueError as e:
        print(f"Input error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

    t_spill, t_full = find_incidents_timing(n, k, capacities)

    print(f"{t_spill} {t_full}")
