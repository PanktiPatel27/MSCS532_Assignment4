
"""
Assignment 4 - Part 2: Task Scheduler Simulation

Non-preemptive scheduling using a binary max-heap priority queue.

Assumption: Every task requires one time unit of execution.
Higher numerical priority is scheduled first.
"""

from priority_queue import Task, PriorityQueue


def simulate_scheduler(tasks):
    """Schedule tasks according to priority and arrival time."""

    pq = PriorityQueue()

    # Sort tasks by arrival time before simulation
    pending_tasks = sorted(
        tasks,
        key=lambda task: (task.arrival_time, task.task_id)
    )

    current_time = 0
    next_task = 0
    schedule = []

    while next_task < len(pending_tasks) or not pq.is_empty():

        # Add all tasks that have arrived
        while (
            next_task < len(pending_tasks)
            and pending_tasks[next_task].arrival_time <= current_time
        ):
            pq.insert(pending_tasks[next_task])
            next_task += 1

        # If no task is ready, advance time to the next arrival
        if pq.is_empty():
            current_time = pending_tasks[next_task].arrival_time
            continue

        # Select the highest-priority available task
        task = pq.extract_max()

        start_time = current_time
        current_time += 1
        completion_time = current_time

        deadline_met = completion_time <= task.deadline

        schedule.append({
            "task_id": task.task_id,
            "priority": task.priority,
            "arrival_time": task.arrival_time,
            "deadline": task.deadline,
            "start_time": start_time,
            "completion_time": completion_time,
            "deadline_met": deadline_met
        })

    return schedule


def main():
    tasks = [
        Task("A", 3, 0, 4),
        Task("B", 5, 1, 3),
        Task("C", 2, 2, 6),
        Task("D", 4, 3, 5),
        Task("E", 5, 1, 4)
    ]

    print("\nTASK SCHEDULER SIMULATION")
    print("=" * 75)
    print("Scheduling policy: Highest priority first")
    print("Execution model: Non-preemptive, one time unit per task")

    results = simulate_scheduler(tasks)

    print("\nSCHEDULING RESULTS")
    print("-" * 75)

    print(
        f"{'Task':<8}{'Priority':<10}{'Arrival':<10}"
        f"{'Deadline':<10}{'Start':<10}{'Finish':<10}{'Status'}"
    )

    for result in results:
        status = "MET" if result["deadline_met"] else "MISSED"

        print(
            f"{result['task_id']:<8}"
            f"{result['priority']:<10}"
            f"{result['arrival_time']:<10}"
            f"{result['deadline']:<10}"
            f"{result['start_time']:<10}"
            f"{result['completion_time']:<10}"
            f"{status}"
        )

    completed = len(results)
    met = sum(result["deadline_met"] for result in results)
    missed = completed - met

    print("\nSCHEDULER SUMMARY")
    print("-" * 75)
    print("Total tasks:", completed)
    print("Deadlines met:", met)
    print("Deadlines missed:", missed)
    print(f"Deadline success rate: {met / completed * 100:.2f}%")


if __name__ == "__main__":
    main()

