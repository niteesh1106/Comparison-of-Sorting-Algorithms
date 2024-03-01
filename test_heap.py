import numpy as np

from heap import *
from bubble_sort import *
from insertion_sort import *
from merge_sort import *
from quick_sort import *

if __name__ == "__main__":
    files = ["title.ratings.txt", "title.ratings_1000.txt", "title.ratings_10000.txt", "title.ratings_100000.txt"]
    print("****QUICK SORT****")
    quickTimes = test_quick_sort()
    print("****MERGE SORT****")
    mergeTimes = test_merge_sort()
    print("****HEAP SORT****")
    heapTimes = test_heap()
    print("****INSERTION SORT****")
    insertionTimes = test_insertion_sort()
    print("****BUBBLE SORT****")
    bubbleTimes = test_bubble_sort()

    functions = ['QuickSort', 'MergeSort', 'HeapSort', 'InsertionSort', 'BubbleSort']
    times = np.array([quickTimes, mergeTimes, heapTimes, insertionTimes, bubbleTimes])

    num_groups = len(times[0])
    num_bars = len(functions)

    indices = np.arange(num_groups)

    bar_width = 0.20

    plt.figure(figsize=(20, 12))
    colors = ['red', 'yellow', 'green', 'blue', 'orange']

    for i in range(num_bars):
        plt.bar(indices + i * bar_width, times[i], width=bar_width, label=functions[i], color=colors[i])

    plt.xlabel('Number of Movies Sorted')
    plt.ylabel('Time in Milliseconds')
    plt.title('Sorting Execution Time by Algorithm and Dataset Size')
    plt.xticks(indices + bar_width, ['1000 Movies', '10000 Movies', '100000 Movies'])
    plt.legend()
    plt.show()
