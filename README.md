# MSCS532_Assignment4
This project explores the design, implementation, and analysis of heap data structures, with a strong focus on both theoretical understanding and practical applications.

## Project Structure
├── heapsort.py                                                                      # Heapsort implementation
├── mergesort.py                                                                            # Merge Sort implementation
├── quicksort.py                                                                            # Quicksort implementation
├── experiment_heapsort.py                                                                  # Performance comparison
├── priority_queue.py                                                                       # Priority Queue + Scheduler simulation
├── Assignment 4 - Report.pdf     # Project documentation
├── README.md                                                                               # Project documentation


## How to Run
### Clone Repository
```
git clone https://github.com/sranabhat51358/MSCS532_Assignment4.git
cd MSCS532_Assignment4
```
### Run Heapsort
```
python heapsort.py
```
#### Output
```
Sorted: [5, 6, 7, 11, 12, 13]
```
### Run Sorting Comparision
```
python experiment_heapsort.py
```

#### Output
```
===== Random Dataset =====

Size: 1000
Heapsort:    0.001171s
Quicksort:   0.000684s
Merge Sort:  0.000826s
Python Sort: 0.000061s

Size: 5000
Heapsort:    0.007550s
Quicksort:   0.004063s
Merge Sort:  0.005205s
Python Sort: 0.000369s

Size: 10000
Heapsort:    0.016650s
Quicksort:   0.008419s
Merge Sort:  0.011270s
Python Sort: 0.000794s

===== Sorted Dataset =====

Size: 1000
Heapsort:    0.001222s
Quicksort:   0.000415s
Merge Sort:  0.000592s
Python Sort: 0.000002s

Size: 5000
Heapsort:    0.008046s
Quicksort:   0.002502s
Merge Sort:  0.003367s
Python Sort: 0.000009s

Size: 10000
Heapsort:    0.017303s
Quicksort:   0.005395s
Merge Sort:  0.006998s
Python Sort: 0.000017s

===== Reverse Dataset =====

Size: 1000
Heapsort:    0.001065s
Quicksort:   0.000411s
Merge Sort:  0.000584s
Python Sort: 0.000002s

Size: 5000
Heapsort:    0.007026s
Quicksort:   0.002503s
Merge Sort:  0.003456s
Python Sort: 0.000010s

Size: 10000
Heapsort:    0.015371s
Quicksort:   0.005415s
Merge Sort:  0.007283s
Python Sort: 0.000018s
```

### Run Priority Queue
```
python priority_queue.py
```

#### Output
```
Initial Task List:
Task ID Priority Arrival    Deadline  
---------------------------------------------
T1      5        08:00:00   10:15:23  
T2      9        08:00:00   11:00:00  
T3      3        08:30:00   12:00:00  
T4      7        08:45:00   11:45:00  
T5      6        09:00:00   13:00:00  
T6      8        09:15:00   12:30:00  
T7      4        09:30:00   14:00:00  
T8      10       09:30:00   11:15:00  
T9      2        10:00:00   15:00:00  
T10     1        10:15:00   16:00:00  
T11     5        10:15:00   12:30:00  
T12     7        10:45:00   13:15:00  
T13     6        11:00:00   14:30:00  
T14     9        11:30:00   13:00:00  
T15     3        12:00:00   15:15:00  

Extracting top 3 highest priority tasks (lowest value = highest priority):
T10 (Priority: 1, Deadline: 16:00:00)
T9 (Priority: 2, Deadline: 15:00:00)
T3 (Priority: 3, Deadline: 12:00:00)
Priority of T8 changed from 10 → 1

Final Priority Queue (Sorted):
Task ID Priority Arrival    Deadline  
---------------------------------------------
T8      1        09:30:00   11:15:00  
T15     3        12:00:00   15:15:00  
T7      4        09:30:00   14:00:00  
T1      5        08:00:00   10:15:23  
T11     5        10:15:00   12:30:00  
T5      6        09:00:00   13:00:00  
T13     6        11:00:00   14:30:00  
T4      7        08:45:00   11:45:00  
T12     7        10:45:00   13:15:00  
T6      8        09:15:00   12:30:00  
T2      9        08:00:00   11:00:00  
T14     9        11:30:00   13:00:00  

Is queue empty? False
```

### Summary

- Heapsort consistently maintains O(n log n) time complexity across all input types (best, average, worst).
- Quicksort performs fastest on average but is sensitive to poor pivot selection (can degrade to O(n²)).
- Merge Sort provides stable and predictable performance but requires O(n) extra space.
- Priority Queue and Scheduler
  - The min-heap efficiently supports dynamic scheduling with:
    - Fast insertion and extraction → O(log n)
  - Priority-based execution ensures:
    - Urgent tasks are handled first
    - Real-world applicability (e.g., OS scheduling, service systems)
  - FIFO behavior for equal priorities ensures fairness and avoids starvation
  - Dynamic priority updates simulate real-world changes (e.g., urgent requests)
  
