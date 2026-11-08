from priority_queue import Task
from task_scheduler import simulate_scheduler


def test_scheduler():
    print("\nSCHEDULER EDGE CASE TESTS")
    print("=" * 50)

    # Test 1: Task arriving later
    tasks = [
        Task("A", 3, 0, 5),
        Task("B", 4, 3, 6)
    ]

    result = simulate_scheduler(tasks)
    assert [r["task_id"] for r in result] == ["A", "B"]
    print("Test 1 - Different arrival times: PASS")

    # Test 2: Equal priority and equal deadline
    tasks = [
        Task("B", 5, 0, 5),
        Task("A", 5, 0, 5)
    ]

    result = simulate_scheduler(tasks)
    assert [r["task_id"] for r in result] == ["A", "B"]
    print("Test 2 - Tie-breaking by task ID: PASS")

    # Test 3: Deadline missed
    tasks = [
        Task("A", 5, 0, 0)
    ]

    result = simulate_scheduler(tasks)
    assert result[0]["deadline_met"] is False
    print("Test 3 - Missed deadline detection: PASS")

    # Test 4: Empty task list
    result = simulate_scheduler([])
    assert result == []
    print("Test 4 - Empty task list: PASS")

    print("\nAll scheduler edge case tests completed.")


if __name__ == "__main__":
    test_scheduler()

