# LeetCode 1672 - Richest Customer Wealth
# Difficulty: Easy


# Approach 1: Your Approach - Loop + sum()
# Time Complexity: O(m * n)
# Space Complexity: O(1)
def maximum_wealth_loop(accounts):
    maximum = 0

    for account in accounts:
        total = sum(account)

        if total > maximum:
            maximum = total

    return maximum


# Approach 2: Using max() + sum()
# Time Complexity: O(m * n)
# Space Complexity: O(1)
def maximum_wealth_max(accounts):
    return max(sum(account) for account in accounts)


# Approach 3: Manual Sum Without sum()
# Time Complexity: O(m * n)
# Space Complexity: O(1)
def maximum_wealth_manual(accounts):
    maximum = 0

    for account in accounts:
        total = 0

        for money in account:
            total += money

        maximum = max(maximum, total)

    return maximum


# Approach 4: List Comprehension
# Time Complexity: O(m * n)
# Space Complexity: O(m)
def maximum_wealth_list(accounts):
    wealth = [sum(account) for account in accounts]

    return max(wealth)


# Approach 5: map() + sum()
# Time Complexity: O(m * n)
# Space Complexity: O(1) Auxiliary
def maximum_wealth_map(accounts):
    return max(map(sum, accounts))
