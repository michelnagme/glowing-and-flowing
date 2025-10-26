import pytest
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

def test_min_inputs():
    n, k = 1, 1
    capacities = [1]

    assert find_incidents_timing(n, k, capacities) == (1, 1)

def test_max_inputs():
    n, k = 100000, 100000           # n = k = 10^5 
    capacities = [1000000000]*n     # c = 10^9 for all tanks

    assert find_incidents_timing(n, k, capacities) == (10000, 10000)

def test_zero_time_overflow():
    n, k = 1, 100000
    capacities = [1]

    assert find_incidents_timing(n, k, capacities) == (0, 0)

def test_zero_time_all_full():
    n, k = 100000, 100000
    capacities = [1]*n

    assert find_incidents_timing(n, k, capacities) == (0, 0)

def test_max_iterations():
    n, k = 100000, 1
    capacities = [1000000000]*n

    assert find_incidents_timing(n, k, capacities) == (1000000000, 1000000000)

def test_n_out_of_specifications():
    n, k = 0, 1
    capacities = []

    with pytest.raises(ValueError):
        find_incidents_timing(n, k, capacities)

    n, k = 100001, 1
    capacities = [10]*n

    with pytest.raises(ValueError):
        find_incidents_timing(n, k, capacities)

def test_k_out_of_specifications():
    n, k = 1, 0
    capacities = [1]

    with pytest.raises(ValueError):
        find_incidents_timing(n, k, capacities)

    n, k = 1, 100001
    capacities = [1]

    with pytest.raises(ValueError):
        find_incidents_timing(n, k, capacities)

def test_capacities_out_of_specifications():
    n, k = 1, 1
    capacities = [1, 1]

    with pytest.raises(ValueError):
        find_incidents_timing(n, k, capacities)

    n, k = 1, 1
    capacities = [0]

    with pytest.raises(ValueError):
        find_incidents_timing(n, k, capacities)

    n, k = 1, 1
    capacities = [1000000001]

    with pytest.raises(ValueError):
        find_incidents_timing(n, k, capacities)
