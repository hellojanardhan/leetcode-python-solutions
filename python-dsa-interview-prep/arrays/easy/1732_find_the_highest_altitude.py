# LeetCode 1732 - Find the Highest Altitude
# Difficulty: Easy


# Approach 1: Running Sum
# Your Approach - Recommended / Optimal
# Time Complexity: O(n)
# Space Complexity: O(1)
def largest_altitude_running_sum(gain):
    current_altitude = 0
    max_altitude = 0

    for value in gain:
        current_altitude += value
        max_altitude = max(max_altitude, current_altitude)

    return max_altitude


# Approach 2: Prefix Sum List
# Time Complexity: O(n)
# Space Complexity: O(n)
def largest_altitude_prefix(gain):
    altitudes = [0]

    for value in gain:
        altitudes.append(altitudes[-1] + value)

    return max(altitudes)


# Approach 3: itertools.accumulate()
# Time Complexity: O(n)
# Space Complexity: O(n)
from itertools import accumulate


def largest_altitude_accumulate(gain):
    altitudes = [0] + list(accumulate(gain))

    return max(altitudes)


# Approach 4: accumulate() without building full altitude list explicitly
# Time Complexity: O(n)
# Space Complexity: O(n) for the generated values consumed by max in practice is not required all at once,
# but conceptually iterator-based auxiliary space is O(1)
from itertools import accumulate


def largest_altitude_accumulate_iterator(gain):
    return max(0, *accumulate(gain))
