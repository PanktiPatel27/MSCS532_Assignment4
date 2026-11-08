import csv
import matplotlib.pyplot as plt
from collections import defaultdict

# Read the benchmark results
results = defaultdict(lambda: defaultdict(list))

with open("results/sorting_benchmark.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        algorithm = row["Algorithm"]
        size = int(row["Input_Size"])
        distribution = row["Distribution"]
        elapsed = float(row["Time_Seconds"])

        results[distribution][algorithm].append((size, elapsed))

# Create one graph for each input distribution
distributions = ["Random", "Sorted", "Reverse"]

for distribution in distributions:
    plt.figure(figsize=(9, 6))

    for algorithm in ["Heapsort", "Quicksort", "Merge Sort"]:
        data = sorted(results[distribution][algorithm])

        sizes = [item[0] for item in data]
        times = [item[1] for item in data]

        plt.plot(sizes, times, marker="o", label=algorithm)

    plt.title(f"Sorting Algorithm Performance - {distribution} Input")
    plt.xlabel("Input Size (number of elements)")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    filename = f"graphs/sorting_{distribution.lower()}.png"
    plt.savefig(filename, dpi=300)
    plt.close()

    print(f"Saved: {filename}")

print("\nAll performance graphs generated successfully.")

