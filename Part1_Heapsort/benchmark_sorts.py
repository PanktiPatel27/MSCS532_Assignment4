"""
Assignment 4 - Part 1
Performance comparison: Heapsort vs Quicksort vs Merge Sort

Tests:
- Random input
- Already sorted input
- Reverse-sorted input

Measures median execution time over repeated runs.
"""

import csv
import random
import statistics
import time
from pathlib import Path

from heapsort import heapsort


def quicksort(arr):
    """In-place Quicksort using median-of-three and 3-way partitioning."""

    def median_of_three(a, b, c):
        return sorted([a, b, c])[1]

    def sort(low, high):
        if low >= high:
            return

        mid = (low + high) // 2
        pivot = median_of_three(arr[low], arr[mid], arr[high])

        # Three-way partition: values below, equal to, and above pivot
        lt = low
        i = low
        gt = high

        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1

        sort(low, lt - 1)
        sort(gt + 1, high)

    sort(0, len(arr) - 1)
    return arr


def merge_sort(arr):
    """Return a sorted copy using Merge Sort."""

    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def measure_time(sort_function, original_data, repetitions=5):
    """Measure median sorting time in seconds."""

    times = []

    for _ in range(repetitions):
        data = original_data.copy()

        start = time.perf_counter()
        result = sort_function(data)
        end = time.perf_counter()

        if result != sorted(original_data):
            raise ValueError(f"{sort_function.__name__} produced an incorrect result.")

        times.append(end - start)

    return statistics.median(times)


def main():
    random.seed(42)

    sizes = [1000, 5000, 10000, 20000]
    distributions = ["Random", "Sorted", "Reverse"]
    algorithms = [
        ("Heapsort", heapsort),
        ("Quicksort", quicksort),
        ("Merge Sort", merge_sort)
    ]

    results = []

    print("\nSORTING ALGORITHM PERFORMANCE COMPARISON")
    print("=" * 65)
    print("Measurements use the median of 5 runs.")
    print("All sorting results are checked for correctness.")

    for size in sizes:
        random_data = [random.randint(0, size * 10) for _ in range(size)]

        input_data = {
            "Random": random_data,
            "Sorted": sorted(random_data),
            "Reverse": sorted(random_data, reverse=True)
        }

        for distribution in distributions:
            data = input_data[distribution]

            print(f"\nInput size: {size:,} | Distribution: {distribution}")

            for algorithm_name, sort_function in algorithms:
                elapsed = measure_time(sort_function, data)

                results.append({
                    "Algorithm": algorithm_name,
                    "Input_Size": size,
                    "Distribution": distribution,
                    "Time_Seconds": elapsed
                })

                print(f"{algorithm_name:12s}: {elapsed:.8f} seconds")

    output_file = Path(__file__).resolve().parent.parent / "results" / "sorting_benchmark.csv"

    with output_file.open("w", newline="") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=[
                "Algorithm",
                "Input_Size",
                "Distribution",
                "Time_Seconds"
            ]
        )
        writer.writeheader()
        writer.writerows(results)

    print("\n" + "=" * 65)
    print(f"Benchmark completed. Results saved to:\n{output_file}")


if __name__ == "__main__":
    main()
