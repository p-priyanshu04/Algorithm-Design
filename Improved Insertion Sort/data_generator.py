from insertion_sort import insertion_sort
from improved_insertion_sort import improved_insertion_sort

import random
import time
import matplotlib.pyplot as plt

sizes = [10, 100, 500, 1000, 2000, 5000, 10000]
basic_times = []
improved_times = []

for size in sizes:
    
    # Generating test cases
    test_data1 = []
    test_data2 = []


    for i in range(size):
        x= random.randint(1, 100000)
        test_data1.append(x)
        test_data2.append(x)

    # Basic Insertion Sort
    t1 = time.time()
    insertion_sort(test_data1)
    t2 = time.time()
    basic_times.append(t2 - t1)

    # Improved Insertion Sort
    t1 = time.time()
    improved_insertion_sort(test_data2)
    t2 = time.time()
    improved_times.append(t2 - t1)

        

# Plotting the results
plt.figure(figsize=(12, 6))
plt.plot(sizes, basic_times, label="Basic Insertion Sort", marker='o')
plt.plot(sizes, improved_times, label="Improved Insertion Sort", marker='o')
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Basic Insertion Sort vs Improved Insertion Sort")
plt.legend()
plt.tight_layout()
plt.show()