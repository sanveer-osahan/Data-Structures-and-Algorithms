def complete_circuit(gas, cost, n):
    gas_in_tank = 0  # Initially the gas in tank is 0.
    deficit = 0  # To keep track of the gas required for previous stations.
    start = 0
    for i in range(n):
        gas_in_tank += gas[i] - cost[i]
        if gas_in_tank < 0:  # If gas in tank is not sufficient.
            start = i + 1  # Mark the new starting station.
            deficit += gas_in_tank  # Keep track of gas required.
            gas_in_tank = 0  # Start from new station, gas in tank will be set to 0.

    return start if gas_in_tank + deficit >= 0 else -1


if __name__ == '__main__':
    Gas = [1, 2, 3, 4, 5]
    Cost = [3, 4, 5, 1, 2]
    N = len(Gas)
    start_station = complete_circuit(Gas, Cost, N)
    if start_station == -1:
        print('There is no possible circuit.')
    else:
        print(f'A circuit can be completed from station {start_station}.')