# LeetCode 881 - Boats to Save People
# Difficulty: Medium


# Approach 1: Sort + Two Pointers
# Recommended / Optimal
# Time Complexity: O(n log n)
# Space Complexity: O(1) algorithmic extra space
def num_rescue_boats_two_pointers(people, limit):
    people.sort()

    left = 0
    right = len(people) - 1
    boats = 0

    while left <= right:
        if left == right:
            boats += 1
            break

        if people[left] + people[right] <= limit:
            left += 1

        right -= 1
        boats += 1

    return boats


# Approach 2: Sort + Two Pointers Without Special left == right Case
# Time Complexity: O(n log n)
# Space Complexity: O(1) algorithmic extra space
def num_rescue_boats_simple(people, limit):
    people.sort()

    left = 0
    right = len(people) - 1
    boats = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1

        right -= 1
        boats += 1

    return boats


# Approach 3: Brute Force Pair Search
# Try to find a partner for each heaviest person
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def num_rescue_boats_bruteforce(people, limit):
    used = [False] * len(people)
    boats = 0

    for i in range(len(people)):
        if used[i]:
            continue

        used[i] = True
        partner = -1

        for j in range(i + 1, len(people)):
            if not used[j] and people[i] + people[j] <= limit:
                partner = j

        if partner != -1:
            used[partner] = True

        boats += 1

    return boats


# Approach 4: Frequency Counting
# Useful only when weight/limit range is small
# Time Complexity: O(n + limit)
# Space Complexity: O(limit)
def num_rescue_boats_frequency(people, limit):
    frequency = [0] * (limit + 1)

    for weight in people:
        frequency[weight] += 1

    light = 1
    heavy = limit
    boats = 0

    while light <= heavy:
        while light <= heavy and frequency[light] == 0:
            light += 1

        while light <= heavy and frequency[heavy] == 0:
            heavy -= 1

        if light > heavy:
            break

        frequency[heavy] -= 1

        if light + heavy <= limit and frequency[light] > 0:
            frequency[light] -= 1

        boats += 1

    return boats
