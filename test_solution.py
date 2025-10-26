from solution import find_incidents_timing


def test_first_example():
    n, k = 4, 1
    capacities = [30, 3, 7, 20]

    assert find_incidents_timing(n, k, capacities) == (10, 30)

def test_second_example():
    n, k = 2, 2
    capacities = [4, 6]

    assert find_incidents_timing(n, k, capacities) == (2, 2)

def test_third_example():
    n, k = 10, 7
    capacities = [100000000, 99999999, 10000000, 1000000, 900000, 90000, 9000, 800, 80, 777]

    assert find_incidents_timing(n, k, capacities) == (61, 14285714)
