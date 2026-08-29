# LeetCode 202 - Happy Number
# Difficulty: Easy
# Recommended Approach: Floyd's Cycle Detection
# Recommended Current-Level Approach: Iterative HashSet


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Recursive HashSet
# Your Approach
# Time Complexity: O(log n)
# Space Complexity: O(log n)
#
# Time Explanation:
# Prati number digits ni process chesi squares sum calculate chestunnam.
# Initial number lo digits count log n ki proportional ga untundi.
# Tarvata generated values small bounded range loki vastayi.
# Repeated number vachina ventane recursion stop avutundi.
# Kabatti standard analysis prakaaram time complexity O(log n).
#
# Space Explanation:
# Generated numbers ni seen set lo store chestunnam.
# Recursive calls kosam call stack koodaa use avutundi.
# Kabatti standard auxiliary space complexity O(log n).
class Solution1:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def check(number):
            if number == 1:
                return True

            if number in seen:
                return False

            seen.add(number)

            total = 0

            for digit in str(number):
                total += int(digit) ** 2

            return check(total)

        return check(n)


# ============================================================


# Approach 2: Iterative HashSet
# Recommended Current-Level Approach
# Time Complexity: O(log n)
# Space Complexity: O(log n)
#
# Time Explanation:
# Prati generated number ni okasari process chestunnam.
# Number 1 ayite True return chestunnam.
# Number repeat ayite cycle undani False return chestunnam.
# Standard analysis prakaaram time complexity O(log n).
#
# Space Explanation:
# Process chesina numbers ni seen set lo store chestunnam.
# Recursion stack use cheyadam ledu.
# Seen values kosam auxiliary space complexity O(log n).
class Solution2:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            total = 0

            for digit in str(n):
                total += int(digit) ** 2

            n = total

        return True


# ============================================================


# Approach 3: Floyd's Cycle Detection
# Recommended Optimal Approach
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Time Explanation:
# Slow pointer okkokka transformation chestundi.
# Fast pointer rendu transformations chestundi.
# Happy number ayite fast pointer 1 ki cherutundi.
# Cycle unte slow mariyu fast pointers kalustayi.
# Standard analysis prakaaram time complexity O(log n).
#
# Space Explanation:
# Set or additional collection create cheyadam ledu.
# Slow, fast mariyu konni temporary variables maatrame use chestunnam.
# Kabatti auxiliary space complexity O(1).
class Solution3:
    def isHappy(self, n: int) -> bool:

        def get_next(number):
            total = 0

            while number > 0:
                digit = number % 10
                total += digit * digit
                number //= 10

            return total

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Iterative HashSet Without String Conversion
# Time Complexity: O(log n)
# Space Complexity: O(log n)
#
# Time Explanation:
# Modulo mariyu integer division use chesi digits extract chestunnam.
# Prati generated number ni seen set tho cycle check chestunnam.
# Standard analysis prakaaram time complexity O(log n).
#
# Space Explanation:
# Generated numbers ni seen set lo store chestunnam.
# Kabatti auxiliary space complexity O(log n).
class Solution4:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            total = 0

            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

        return True


# ============================================================


# Approach 5: Detect the Known Unhappy Cycle at 4
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Time Explanation:
# Happy number sequence 1 daggara stop avutundi.
# Unhappy number sequence known cycle lo 4 daggara enter avutundi.
# Kabatti n 1 ledaa 4 ayye varaku process chestunnam.
# Standard analysis prakaaram time complexity O(log n).
#
# Space Explanation:
# Set or recursion stack use cheyadam ledu.
# Konni variables maatrame use chestunnam.
# Kabatti auxiliary space complexity O(1).
class Solution5:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:
            total = 0

            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

        return n == 1
