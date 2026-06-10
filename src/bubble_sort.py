"""
Time Complexity:
    Basic:
        O(n²) - every element is compared to every other element in the worst case
    Optimized:
        - Best Case: O(n)   - detects sorted array after a single pass
        - Average/Worst Case: O(n²)

Space Complexity: O(1) - in-place sorting

Stability: Bubble Sort IS stable. Equal elements are not swapped
"""

# Basic Bubble Sort:

def bubble_sort_basic(arr: list[int]) -> list[int]:
    n = len(arr)

    for i in range(n - 1):
        
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Optimized Bubble Sort:

def bubble_sort_optimized(arr: list[int]) -> list[int]:
    """
        Optimised Bubble Sort using flag to track if swaps were made.
    """
    n = len(arr)

    for i in range(n - 1):

        swapped = False

        for j in range(n - 1 - i):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr