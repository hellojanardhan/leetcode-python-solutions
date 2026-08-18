# LeetCode 119 - Pascal's Triangle II
# Difficulty: Easy


# Approach 1: Build Entire Pascal Triangle
# Your Approach
# Time Complexity: O(rowIndex^2)
# Space Complexity: O(rowIndex^2)
def get_row_full_triangle(rowIndex):
    result = [[1]]

    for _ in range(rowIndex):
        previous = result[-1]

        new_row = [1] * (len(previous) + 1)

        for j in range(len(previous) - 1):
            new_row[j + 1] = previous[j] + previous[j + 1]

        result.append(new_row)

    return result[rowIndex]


# Approach 2: Keep Only Previous Row
# Better Approach
# Time Complexity: O(rowIndex^2)
# Space Complexity: O(rowIndex)
def get_row_previous_only(rowIndex):
    row = [1]

    for _ in range(rowIndex):
        new_row = [1] * (len(row) + 1)

        for j in range(len(row) - 1):
            new_row[j + 1] = row[j] + row[j + 1]

        row = new_row

    return row


# Approach 3: In-place Update from Right to Left
# Recommended Interview Solution
# Time Complexity: O(rowIndex^2)
# Space Complexity: O(rowIndex)
def get_row_inplace(rowIndex):
    row = [1] * (rowIndex + 1)

    for i in range(2, rowIndex + 1):
        for j in range(i - 1, 0, -1):
            row[j] = row[j] + row[j - 1]

    return row


# Approach 4: Combination Formula
# Best Time Complexity
# Time Complexity: O(rowIndex)
# Space Complexity: O(rowIndex)
def get_row_combination(rowIndex):
    row = [1]
    value = 1

    for k in range(1, rowIndex + 1):
        value = value * (rowIndex - k + 1) // k
        row.append(value)

    return row
