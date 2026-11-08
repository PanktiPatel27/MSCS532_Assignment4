"""
Assignment 4 - Part 1: Heapsort Implementation

This program implements Heapsort using a max-heap.
It includes:
1. Max-heap construction
2. Heapify operation
3. Heapsort sorting algorithm
4. Test cases to verify correctness
"""

def heapify(arr, n, root):
    """
    Maintain the max-heap property for a subtree.

    arr: list of elements
    n: current heap size
    root: index of the subtree root
    """
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    # Check whether the left child is larger than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check whether the right child is larger than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the root is not the largest, swap and continue heapifying
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, n, largest)


def heapsort(arr):
    """
    Sort a list in ascending order using Heapsort.

    The algorithm builds a max-heap and repeatedly moves
    the largest element to the end of the list.

    Returns the sorted list.
    """
    n = len(arr)

    # Phase 1: Build a max-heap
    # Start from the last non-leaf node and move toward the root
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Phase 2: Extract the maximum element repeatedly
    for i in range(n - 1, 0, -1):
        # Move the maximum element to its final position
        arr[0], arr[i] = arr[i], arr[0]

        # Restore the max-heap property in the reduced heap
        heapify(arr, i, 0)

    return arr


def run_tests():
    """Run test cases to verify that Heapsort works correctly."""

    test_cases = [
        [12, 11, 13, 5, 6, 7],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [10, 10, 5, 5, 1, 1],
        [42],
        [],
        [3, -1, 8, 0, -5, 12]
    ]

    print("\nHEAPSORT IMPLEMENTATION")
    print("=" * 50)

    for index, test in enumerate(test_cases, start=1):
        original = test.copy()
        result = heapsort(test.copy())
        expected = sorted(original)

        status = "PASS" if result == expected else "FAIL"

        print(f"\nTest {index}: {original}")
        print(f"Sorted:  {result}")
        print(f"Expected: {expected}")
        print(f"Status: {status}")

    print("\nAll test cases completed.")


if __name__ == "__main__":
    run_tests()
