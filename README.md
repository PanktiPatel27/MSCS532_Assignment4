# Assignment 4 — Heap Data Structures: Implementation, Analysis, and Applications

A Python project covering two core data-structure topics:

- Heap-based sorting and empirical performance analysis
- Priority-queue design and a task-scheduling simulation

> The project uses measured runtime data from the included experiments. Sorting timings are the median of five runs, and every sorting result is validated against Python's `sorted()` output.

## Overview

This repository contains two major parts:

1. **Heapsort and sorting analysis**
   - Max-heap-based Heapsort implementation
   - Empirical comparison with median-of-three three-way Quicksort and Merge Sort

2. **Priority queue and task scheduler**
   - Array-backed binary max-priority queue
   - Non-preemptive task scheduling simulation with deadline checking

## Repository structure

```text
Assignment4/
├── Part1_Heapsort/
│   ├── heapsort.py
│   └── benchmark_sorts.py
├── Part2_PriorityQueue/
│   ├── priority_queue.py
│   ├── task_scheduler.py
│   ├── test_scheduler.py
│   └── save_scheduler_results.py
├── results/
│   ├── sorting_benchmark.csv
│   └── scheduler_results.csv
├── graphs/
│   ├── sorting_random.png
│   ├── sorting_sorted.png
│   └── sorting_reverse.png
├── screenshots/
├── plot_results.py
├── README.md
├── Assignment4_Heap_Data_Structures_Report.docx
├── .gitignore
└── .venv/
```

## Requirements

- Python 3.14.7 was used for the reported project run
- `matplotlib` is required only to regenerate the sorting graphs
- The local virtual environment should not be committed

Install the plotting dependency:

```bash
python -m pip install matplotlib
```

## Setup

From the repository root:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install matplotlib
```

## Part 1 — Heapsort

### Run correctness tests

```bash
python Part1_Heapsort/heapsort.py
```

The test suite reported seven passing cases, including:

- ordinary input
- sorted input
- reverse-sorted input
- duplicates
- single-item input
- empty list
- negative values

### Run the benchmark

```bash
python Part1_Heapsort/benchmark_sorts.py
```

The benchmark evaluates:

- Input sizes: 1,000, 5,000, 10,000, and 20,000
- Distributions: random, sorted, and reverse-sorted
- Algorithms: Heapsort, median-of-three three-way Quicksort, and Merge Sort
- Repetitions: five; timing reported as the median
- Correctness: each output is validated against `sorted(original_data)`

Results are written to:

```text
results/sorting_benchmark.csv
```

## Part 2 — Priority Queue and Scheduler

### Run priority queue tests

```bash
python Part2_PriorityQueue/priority_queue.py
```

### Run scheduler edge-case tests

```bash
python Part2_PriorityQueue/test_scheduler.py
```

### Run the scheduler simulation

```bash
python Part2_PriorityQueue/task_scheduler.py
```

### Save scheduler sample results

```bash
python Part2_PriorityQueue/save_scheduler_results.py
```

The scheduler output is written to:

```text
results/scheduler_results.csv
```

### Priority ordering

The max-priority queue uses the following ordering:

1. Higher numeric priority first
2. Earlier deadline first when priorities tie
3. Earlier arrival time next
4. Lexicographically smaller task ID as the final tie-breaker

The scheduler is non-preemptive and assumes each task takes one simulated time unit. A deadline is considered met when completion time is less than or equal to the task deadline.

## Complexity summary

| Component | Time complexity |
| --- | ---: |
| Build max-heap | O(n) |
| Heapsort | O(n log n) best, average, and worst |
| Priority queue insert | O(log n) |
| Priority queue extract maximum | O(log n) |
| Increase/decrease key | O(log n) |
| Check empty / queue length | O(1) |
| Scheduler overall | O(n log n), including arrival-time sorting |

The Heapsort implementation uses recursive `heapify`, so its recursion stack can require O(log n) auxiliary space. The array itself is sorted in place.

## Experimental summary

Observed results from the project run:

- Random inputs: Quicksort was fastest at each tested input size
- Sorted inputs: Merge Sort was fastest at each tested input size
- Reverse-sorted inputs: Merge Sort was fastest at each tested input size
- At 20,000 random elements: Heapsort 0.03644696 s; Quicksort 0.02238062 s; Merge Sort 0.02430512 s
- At 20,000 sorted elements: Heapsort 0.03839833 s; Quicksort 0.09632450 s; Merge Sort 0.01569554 s
- At 20,000 reverse-sorted elements: Heapsort 0.03362017 s; Quicksort 0.07097483 s; Merge Sort 0.01651667 s
- Scheduler sample: 5 tasks scheduled, 5 deadlines met, 0 missed; success rate 100.00%

These values reflect the tested machine and workload, not universal performance guarantees.

## Graphs

The `graphs/` directory contains the following generated plots:

- `sorting_random.png`
- `sorting_sorted.png`
- `sorting_reverse.png`

These graphs plot median execution time against input size for all three sorting algorithms.

## Results and report

- `results/sorting_benchmark.csv` — measured sorting timings
- `results/scheduler_results.csv` — task schedule and deadline outcomes
- `Assignment4_Heap_Data_Structures_Report.docx` — detailed project report

## Notes

- Run commands from the repository root unless otherwise specified
- Do not commit `venv/`, `.DS_Store`, or Python cache directories
- Re-run the benchmark if measurements need to be reproduced on another computer; timings vary by hardware and system load

## Quick start

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install matplotlib
python Part1_Heapsort/heapsort.py
python Part1_Heapsort/benchmark_sorts.py
python Part2_PriorityQueue/priority_queue.py
python Part2_PriorityQueue/test_scheduler.py
python Part2_PriorityQueue/task_scheduler.py
```
