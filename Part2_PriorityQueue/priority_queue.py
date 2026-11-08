
"""
Assignment 4 - Part 2: Priority Queue Using a Binary Max-Heap

Higher numerical priority is processed first.
Tie-breaking:
1. Earlier deadline
2. Earlier arrival time
3. Task ID
"""

from dataclasses import dataclass


@dataclass
class Task:
    task_id: str
    priority: int
    arrival_time: int
    deadline: int

    def __repr__(self):
        return (
            f"Task(id={self.task_id}, priority={self.priority}, "
            f"arrival={self.arrival_time}, deadline={self.deadline})"
        )


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.position = {}

    def _higher_priority(self, task1, task2):
        """Return True if task1 should appear before task2."""
        if task1.priority != task2.priority:
            return task1.priority > task2.priority

        if task1.deadline != task2.deadline:
            return task1.deadline < task2.deadline

        if task1.arrival_time != task2.arrival_time:
            return task1.arrival_time < task2.arrival_time

        return task1.task_id < task2.task_id

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.position[self.heap[i].task_id] = i
        self.position[self.heap[j].task_id] = j

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self._higher_priority(
                self.heap[index], self.heap[parent]
            ):
                self._swap(index, parent)
                index = parent
            else:
                break

    def _sift_down(self, index):
        size = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if (
                left < size
                and self._higher_priority(
                    self.heap[left], self.heap[largest]
                )
            ):
                largest = left

            if (
                right < size
                and self._higher_priority(
                    self.heap[right], self.heap[largest]
                )
            ):
                largest = right

            if largest == index:
                break

            self._swap(index, largest)
            index = largest

    def insert(self, task):
        if task.task_id in self.position:
            raise ValueError("Task ID already exists.")

        self.heap.append(task)
        index = len(self.heap) - 1
        self.position[task.task_id] = index
        self._sift_up(index)

    def extract_max(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty.")

        maximum = self.heap[0]
        last = self.heap.pop()
        del self.position[maximum.task_id]

        if self.heap:
            self.heap[0] = last
            self.position[last.task_id] = 0
            self._sift_down(0)

        return maximum

    def increase_key(self, task_id, new_priority):
        if task_id not in self.position:
            raise KeyError("Task ID not found.")

        index = self.position[task_id]
        task = self.heap[index]

        if new_priority < task.priority:
            raise ValueError("New priority must be greater.")

        task.priority = new_priority
        self._sift_up(index)

    def decrease_key(self, task_id, new_priority):
        if task_id not in self.position:
            raise KeyError("Task ID not found.")

        index = self.position[task_id]
        task = self.heap[index]

        if new_priority > task.priority:
            raise ValueError("New priority must be smaller.")

        task.priority = new_priority
        self._sift_down(index)

    def is_empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)


def run_tests():
    print("\nBINARY MAX-HEAP PRIORITY QUEUE")
    print("=" * 55)

    pq = PriorityQueue()

    tasks = [
        Task("T1", 3, 1, 10),
        Task("T2", 5, 2, 8),
        Task("T3", 2, 3, 12),
        Task("T4", 4, 4, 9),
    ]

    print("\nInsert tests:")
    for task in tasks:
        pq.insert(task)
        print("Inserted:", task)

    print("\nQueue size:", len(pq))
    print("Is empty:", pq.is_empty())

    print("\nIncrease-key test:")
    pq.increase_key("T3", 6)
    print("Increased T3 priority to 6")

    print("\nDecrease-key test:")
    pq.decrease_key("T3", 1)
    print("Decreased T3 priority to 1")

    print("\nExtract-max tests:")
    while not pq.is_empty():
        print("Extracted:", pq.extract_max())

    print("\nIs empty after extraction:", pq.is_empty())

    print("\nAll priority queue tests completed.")


if __name__ == "__main__":
    run_tests()

