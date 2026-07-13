"""
Big O Practice Examples

Complexity Ranking (Best -> Worst)

1.  O(1)          Constant          ⭐⭐⭐⭐⭐
2.  O(log n)      Logarithmic       ⭐⭐⭐⭐⭐
3.  O(n)          Linear            ⭐⭐⭐⭐
4.  O(n log n)    Linearithmic      ⭐⭐⭐⭐
5.  O(n²)         Quadratic          ⭐⭐
6.  O(n³)         Cubic              ⭐
7.  O(2ⁿ)         Exponential        💀
8.  O(n!)         Factorial          ☠️


Rules:
- Sequential operations add:
      O(n) + O(m) = O(n + m)

- Nested loops multiply:
      O(n) * O(m) = O(nm)

- Remove constants:
      O(5n) = O(n)

- Keep the biggest growing term:
      O(n + n²) = O(n²)

"""


# ===================================================
# Example 1
# Complexity:
# O(n)
#
# Ranking:
# Better than O(n²)
# Worse than O(log n)
#
# One loop
# ===================================================

def example1(numbers):

    for number in numbers:
        print(number)



# ===================================================
# Example 2
# Complexity:
# O(n²)
#
# Ranking:
# Slower than O(n)
# Faster than O(n³)
#
# Nested loop
# ===================================================

def example2(numbers):

    for i in numbers:
        for j in numbers:
            pass



# ===================================================
# Example 3
# Complexity:
# O(n + m)
#
# Ranking:
# Usually better than O(nm)
#
# Two independent loops
# ===================================================

def example3(users, orders):

    for user in users:
        pass

    for order in orders:
        pass



# ===================================================
# Example 4
# Complexity:
# O(nm)
#
# If n == m:
# O(n²)
#
# Nested loops on different data
# ===================================================

def example4(users, orders):

    for user in users:

        for order in orders:
            pass



# ===================================================
# Example 5
#
# Complexity calculation:
#
# First loop:
# O(n)
#
# Nested loop:
# O(n²)
#
# Total:
# O(n + n²)
#
# Remove smaller term:
# O(n²)
#
# ===================================================

def example5(numbers):

    for number in numbers:
        pass


    for i in numbers:

        for j in numbers:
            pass



# ===================================================
# Example 6
#
# Complexity:
# O(log n)
#
# Ranking:
# One of the fastest
#
# Why?
# Input reduces by half:
#
# n
# n/2
# n/4
# n/8
#
# ===================================================

def example6(numbers):

    i = len(numbers)

    while i > 1:

        i = i // 2



# ===================================================
# Example 7
#
# Complexity:
# O(n log n)
#
# Calculation:
#
# Outer loop:
# O(n)
#
# Inner loop:
# O(log n)
#
# Multiply:
# O(n * log n)
#
# ===================================================

def example7(numbers):

    n = len(numbers)

    for i in range(n):

        j = 1

        while j < n:

            j = j * 2



# ===================================================
# Example 8
#
# Complexity:
# O(nm)
#
# Real-world example:
# Users -> Orders
#
# Every user checks every order
#
# ===================================================

def example8(users):

    for user in users:

        for order in user["orders"]:
            pass



# ===================================================
# Example 9
#
# Complexity:
#
# Sorting:
# O(n log n)
#
# Loop:
# O(n)
#
# Total:
# O(n log n + n)
#
# Remove smaller:
# O(n log n)
#
# ===================================================

def example9(numbers):

    numbers.sort()

    for number in numbers:
        pass



# ===================================================
# Example 10
#
# Complexity:
#
# Loop:
# O(n)
#
# Sort:
# O(n log n)
#
# Nested loop:
# O(n²)
#
# Total:
#
# O(n + n log n + n²)
#
# Final:
# O(n²)
#
# ===================================================

def example10(numbers):

    # O(n)
    for number in numbers:
        pass


    # O(n log n)
    numbers.sort()


    # O(n²)
    for i in numbers:

        for j in numbers:
            pass



# ===================================================
# BONUS EXAMPLES
# Worse complexities
# ===================================================


# ===================================================
# Example 11
#
# Complexity:
# O(2ⁿ)
#
# Exponential
#
# Very bad
#
# Each item creates 2 choices
#
# Example:
# Include item
# Exclude item
#
# ===================================================

def example11_recursive(n):

    if n <= 1:
        return n

    return (
        example11_recursive(n-1)
        +
        example11_recursive(n-2)
    )



# ===================================================
# Example 12
#
# Complexity:
# O(n!)
#
# Worst practical complexity
#
# Example:
# Generate every possible arrangement
#
# 5 items:
# 120 possibilities
#
# 10 items:
# 3,628,800 possibilities
#
# ===================================================

def example12_factorial(items):

    if len(items) <= 1:
        return [items]

    result = []

    for item in items:

        remaining = [
            x for x in items
            if x != item
        ]

        for permutation in example12_factorial(remaining):

            result.append(
                [item] + permutation
            )

    return result