# LeetCode 118 - Pascal's Triangle
# Difficulty: Easy


# Approach 1: Build Using Previous Row
# Your Approach - Simplified
# Time Complexity: O(numRows^2)
# Space Complexity: O(numRows^2)
def generate_pascal_previous_row(numRows):
    result = [[1]]

    for _ in range(numRows - 1):
        previous = result[-1]

        new_row = [1] * (len(previous) + 1)

        for j in range(len(previous) - 1):
            new_row[j + 1] = previous[j] + previous[j + 1]

        result.append(new_row)

    return result


# Approach 2: Build Row by Row Using Indices
# Recommended Interview Solution
# Time Complexity: O(numRows^2)
# Space Complexity: O(numRows^2)
def generate_pascal_index(numRows):
    result = []

    for row in range(numRows):
        current = [1] * (row + 1)

        for col in range(1, row):
            current[col] = (
                result[row - 1][col - 1]
                + result[row - 1][col]
            )

        result.append(current)

    return result


# Approach 3: Using zip()
# Pythonic Approach
# Time Complexity: O(numRows^2)
# Space Complexity: O(numRows^2)
def generate_pascal_zip(numRows):
    result = [[1]]

    for _ in range(numRows - 1):
        previous = result[-1]

        middle = [
            left + right
            for left, right in zip(previous, previous[1:])
        ]

        result.append([1] + middle + [1])

    return result


# Approach 4: Combination Formula
# C(n, k) calculated from previous value
# Time Complexity: O(numRows^2)
# Space Complexity: O(numRows^2)
def generate_pascal_combination(numRows):
    result = []

    for row in range(numRows):
        current = [1]
        value = 1

        for col in range(1, row + 1):
            value = value * (row - col + 1) // col
            current.append(value)

        result.append(current)

    return result
