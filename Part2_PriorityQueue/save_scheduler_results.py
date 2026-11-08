import csv
import os
from priority_queue import Task
from task_scheduler import simulate_scheduler

tasks = [
    Task("A", 3, 0, 4),
    Task("B", 5, 1, 3),
    Task("C", 2, 2, 6),
    Task("D", 4, 3, 5),
    Task("E", 5, 1, 4)
]

results = simulate_scheduler(tasks)

os.makedirs("../results", exist_ok=True)

filename = "../results/scheduler_results.csv"

with open(filename, "w", newline="") as file:
    fieldnames = [
        "task_id",
        "priority",
        "arrival_time",
        "deadline",
        "start_time",
        "completion_time",
        "deadline_met"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

completed = len(results)
met = sum(row["deadline_met"] for row in results)

print("Scheduler results saved successfully.")
print("File:", filename)
print("Total tasks:", completed)
print("Deadlines met:", met)
print("Deadlines missed:", completed - met)
print(f"Success rate: {met / completed * 100:.2f}%")
