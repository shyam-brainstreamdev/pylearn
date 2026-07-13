"""
Space Complexity Demonstration

Best -> Worst (common)

O(1)
    Constant memory
    Example: variables only

O(log n)
    Recursive stack (binary search)

O(n)
    Store one extra collection

O(n²)
    Store matrix/table

Space complexity measures:
"How much EXTRA memory is created as input grows?"
"""

import tracemalloc


def measure_memory(func, *args):

    tracemalloc.start()

    func(*args)

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return peak / (1024 * 1024)  # MB



# =====================================================
# Example 1
#
# Space: O(1)
#
# Only variables
# =====================================================

def constant_space(numbers):

    total = 0

    for number in numbers:
        total += number

    return total



# =====================================================
# Example 2
#
# Space: O(n)
#
# Create another list
# =====================================================

def linear_space(numbers):

    result = []

    for number in numbers:
        result.append(number * 2)

    return result



# =====================================================
# Example 3
#
# Space: O(n)
#
# Dictionary grows with input
# =====================================================

def dictionary_space(numbers):

    result = {}

    for number in numbers:
        result[number] = number * 2

    return result



# =====================================================
# Example 4
#
# Space: O(n²)
#
# Matrix creation
#
# Example:
#
# [
#   [0,0,0],
#   [0,0,0],
#   [0,0,0]
# ]
#
# =====================================================

def quadratic_space(numbers):

    n = len(numbers)

    matrix = []

    for i in range(n):

        row = []

        for j in range(n):

            row.append(0)

        matrix.append(row)

    return matrix



if __name__ == "__main__":


    sizes = [
        1000,
        5000,
        10000
    ]


    for size in sizes:

        print("\n" + "=" * 50)

        print(f"Input size: {size:,}")

        numbers = list(range(size))


        memory = measure_memory(
            constant_space,
            numbers
        )

        print(
            f"O(1)   Constant Space      : {memory:.4f} MB"
        )


        memory = measure_memory(
            linear_space,
            numbers
        )

        print(
            f"O(n)   List Space         : {memory:.4f} MB"
        )


        memory = measure_memory(
            dictionary_space,
            numbers
        )

        print(
            f"O(n)   Dictionary Space   : {memory:.4f} MB"
        )


        # O(n²) grows very fast
        # Only run for small sizes

        if size <= 1000:

            memory = measure_memory(
                quadratic_space,
                numbers
            )

            print(
                f"O(n²)  Matrix Space       : {memory:.4f} MB"
            )