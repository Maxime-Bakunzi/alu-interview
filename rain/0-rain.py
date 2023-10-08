#!usr/bin/python3

def rain(walls):
    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    # Initialize left_max array
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Initialize right_max array
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    total_water = 0
    for i in range(n):
        total_water += min(left_max[i], right_max[i]) - walls[i]

    return total_water

# Example usage:
walls1 = []
print(rain(walls1))  # Output: 0

walls2 = [2, 0, 2]
print(rain(walls2))  # Output: 2

walls3 = [0, 1, 0, 2, 0, 3, 0, 4]
print(rain(walls3))  # Output: 6

walls4 = [1, 1, 2, 0, 1, 1, 1]
print(rain(walls4))  # Output: 0

walls5 = [0, 2, 1, 0, 1, 3, 1, 2, 1, 1, 2, 1]
print(rain(walls5))  # Output: 6

walls6 = [2, 0, 0, 0, 0, 3, 0]
print(rain(walls6))  # Output: 10

walls7 = [1]
print(rain(walls7))  # Output: 0

walls8 = [3, 3]
print(rain(walls8))  # Output: 0
