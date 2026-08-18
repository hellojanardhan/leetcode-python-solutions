# LeetCode 66 - Plus One
# Difficulty: Easy


# Approach 1: Right-to-Left Carry
# Your Approach - Simplified / Recommended
# Time Complexity: O(n)
# Space Complexity: O(1) auxiliary
def plus_one_carry(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits

        digits[i] = 0

    return [1] + digits


# Approach 2: Your Original Logic with all()
# Time Complexity: O(n)
# Space Complexity: O(1) auxiliary
def plus_one_all(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            break

    result = all(num == 0 for num in digits)

    if result:
        digits.insert(0, 1)

    return digits


# Approach 3: Explicit Carry Variable
# Time Complexity: O(n)
# Space Complexity: O(1) auxiliary
def plus_one_explicit_carry(digits):
    carry = 1

    for i in range(len(digits) - 1, -1, -1):
        total = digits[i] + carry

        digits[i] = total % 10
        carry = total // 10

        if carry == 0:
            break

    if carry:
        digits.insert(0, carry)

    return digits


# Approach 4: Convert Digits to Integer
# Python-specific approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def plus_one_integer(digits):
    number = int("".join(map(str, digits)))
    number += 1

    return list(map(int, str(number)))
