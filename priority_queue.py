from datetime import datetime
import heapq

# -----------------------------
# Task Class
# -----------------------------
class Task:
    """
    Represents a task with:
    - task_id: unique identifier
    - priority: lower value = higher priority
    - arrival_time: when task enters system
    - deadline: task completion deadline
    """

    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        """
        Defines comparison for heap:
        - First compare priority
        - If equal, compare arrival time (FIFO behavior)
        """
        if self.priority == other.priority:
            return self.arrival_time < other.arrival_time
        return self.priority < other.priority

    def __repr__(self):
        """
        String representation for debugging
        """
        return (f"Task({self.task_id}, priority={self.priority}, "
                f"arrival={self.arrival_time.strftime('%H:%M:%S')}, "
                f"deadline={self.deadline.strftime('%H:%M:%S')})")


# -----------------------------
# Priority Queue Class (Min-Heap)
# -----------------------------
class PriorityQueue:
    """
    Implements a priority queue using a binary min-heap.
    """

    def __init__(self):
        self.heap = []                 # underlying heap
        self.entry_finder = {}         # maps task_id -> task object

    def insert(self, task):
        """
        Insert a task into the priority queue.
        Time Complexity: O(log n)
        """
        heapq.heappush(self.heap, task)
        self.entry_finder[task.task_id] = task

    def extract_min(self):
        """
        Remove and return highest priority task (lowest value).
        Time Complexity: O(log n)
        """
        while self.heap:
            task = heapq.heappop(self.heap)
            if task.task_id in self.entry_finder:
                del self.entry_finder[task.task_id]
                return task
        return None

    def change_priority(self, task_id, new_priority):
        """
        Update the priority of a task.
        Time Complexity: O(n) + O(log n)
        """
        if task_id not in self.entry_finder:
            print(f"Task {task_id} not found!")
            return

        task = self.entry_finder[task_id]
        old_priority = task.priority

        # Remove and reinsert to maintain heap property
        self.heap.remove(task)      # O(n)
        heapq.heapify(self.heap)    # restore heap after removal

        task.priority = new_priority
        heapq.heappush(self.heap, task)  # O(log n)

        print(f"Priority of {task_id} changed from {old_priority} → {new_priority}")

    def is_empty(self):
        """
        Check if queue is empty.
        Time Complexity: O(1)
        """
        return len(self.entry_finder) == 0


# -----------------------------
# Utility Function to Print Tasks
# -----------------------------
def print_task_list(task_list, title):
    """
    Prints tasks in a formatted table.
    """
    print(f"\n{title}:")
    print(f"{'Task ID':<7} {'Priority':<8} {'Arrival':<10} {'Deadline':<10}")
    print("-" * 45)

    for task in task_list:
        print(f"{task.task_id:<7} {task.priority:<8} "
              f"{task.arrival_time.strftime('%H:%M:%S'):<10} "
              f"{task.deadline.strftime('%H:%M:%S'):<10}")


# -----------------------------
# Main Simulation
# -----------------------------
if __name__ == "__main__":

    pq = PriorityQueue()

    # Predefined 15 tasks (as per assignment requirement)
    tasks_data = [
        ("T1", 5, "2026-03-25 08:00:00", "2026-03-25 10:15:23"),
        ("T2", 9, "2026-03-25 08:00:00", "2026-03-25 11:00:00"),
        ("T3", 3, "2026-03-25 08:30:00", "2026-03-25 12:00:00"),
        ("T4", 7, "2026-03-25 08:45:00", "2026-03-25 11:45:00"),
        ("T5", 6, "2026-03-25 09:00:00", "2026-03-25 13:00:00"),
        ("T6", 8, "2026-03-25 09:15:00", "2026-03-25 12:30:00"),
        ("T7", 4, "2026-03-25 09:30:00", "2026-03-25 14:00:00"),
        ("T8", 10, "2026-03-25 09:30:00", "2026-03-25 11:15:00"),
        ("T9", 2, "2026-03-25 10:00:00", "2026-03-25 15:00:00"),
        ("T10", 1, "2026-03-25 10:15:00", "2026-03-25 16:00:00"),
        ("T11", 5, "2026-03-25 10:15:00", "2026-03-25 12:30:00"),
        ("T12", 7, "2026-03-25 10:45:00", "2026-03-25 13:15:00"),
        ("T13", 6, "2026-03-25 11:00:00", "2026-03-25 14:30:00"),
        ("T14", 9, "2026-03-25 11:30:00", "2026-03-25 13:00:00"),
        ("T15", 3, "2026-03-25 12:00:00", "2026-03-25 15:15:00"),
    ]

    # -----------------------------
    # Insert and Print Initial Tasks
    # -----------------------------
    task_objects = []

    for task_id, priority, arrival_str, deadline_str in tasks_data:
        arrival = datetime.strptime(arrival_str, "%Y-%m-%d %H:%M:%S")
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M:%S")

        task = Task(task_id, priority, arrival, deadline)
        pq.insert(task)
        task_objects.append(task)

    print_task_list(task_objects, "Initial Task List")

    # -----------------------------
    # Extract Top 3 Tasks
    # -----------------------------
    print("\nExtracting top 3 highest priority tasks (lowest value = highest priority):")

    extracted_tasks = []
    for _ in range(3):
        task = pq.extract_min()
        extracted_tasks.append(task)
        print(f"{task.task_id} (Priority: {task.priority}, Deadline: {task.deadline.strftime('%H:%M:%S')})")

    # -----------------------------
    # Change Priority Example
    # -----------------------------
    pq.change_priority("T8", 1)

    # -----------------------------
    # Print Final Queue (Sorted)
    # -----------------------------
    remaining_tasks = list(pq.entry_finder.values())
    sorted_final = sorted(remaining_tasks, key=lambda t: (t.priority, t.arrival_time))

    print_task_list(sorted_final, "Final Priority Queue (Sorted)")

    # -----------------------------
    # Check if Empty
    # -----------------------------
    print("\nIs queue empty?", pq.is_empty())
