import math
import time

from matplotlib import pyplot as plt


class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return math.floor((i - 1) / 2)

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def maxHeapify(self, i):
        l = self.leftChild(i)
        r = self.rightChild(i)
        largest = i
        if l < len(self.heap) and self.heap[l] > self.heap[largest]:
            largest = l
        if r < len(self.heap) and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.maxHeapify(largest)

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def Print(self):
        for i in range(len(self.heap)):
            print(self.heap[i], end=" ")
        print("print")

    def maxHeap(arr):
        n = len(arr)
        maxHeap = MaxHeap()
        for i in range(n):
            maxHeap.insert(arr[i])
        print(maxHeap)
        return maxHeap

    def remove(self):
        if len(self.heap) == 0:
            return None
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.maxHeapify(0)
        return max_val


def sort_movies_batch(names, ratings):
    n = len(names)
    ratings1 = ratings.copy()
    heap = MaxHeap.maxHeap(ratings1)
    sorted_names = []
    for i in range(n):
        max_val = heap.remove()
        index = ratings1.index(max_val)
        sorted_names.append(names[index])
        ratings1[index] = -1
    return sorted_names


def sort_movie_incre(names, ratings):
    n = len(names)
    ratings2 = ratings.copy()
    heap = MaxHeap()
    sorted_names = []
    for i in range(n):
        heap.insert(ratings2[i])
    for i in range(n):
        max_val = heap.remove()
        index = ratings2.index(max_val)
        sorted_names.append(names[index])
        ratings2[index] = -1  # mark as visited
    return sorted_names


def sort_movies(filename):
    a_file = open(filename)
    names, ratings = [], []
    next(a_file)
    name_score_dict = {}
    for line in a_file:
        temp = line.rstrip().split('; ')
        names.append(temp[0])  # key: name
        ratings.append(float(temp[1]))  # name: rating
        name_score_dict[temp[0]] = float(temp[1])

    sort_movie_incre(names, ratings)


def sort_movies_Batch_version():
    a_file = open("title.ratings.txt")
    names, ratings = [], []
    next(a_file)
    name_score_dict = {}
    for line in a_file:
        temp = line.rstrip().split('; ')
        names.append(temp[0])  # key: name
        ratings.append(float(temp[1]))  # name: rating
        name_score_dict[temp[0]] = float(temp[1])

    sorted_names1 = sort_movies_batch(names, ratings)

    sorted_1 = []
    for item in sorted_names1:
        sorted_1.append(name_score_dict[item])

    sorted_true = [9.4, 9.3, 9.2, 9.1, 9.0, 9.0, 8.8, 8.8, 8.8, 8.8, 8.7, 8.7,
                   8.6, 8.6, 8.5, 8.5, 8.4, 8.4, 8.4, 8.4, 8.4, 8.4, 8.3, 8.2, 8.1, 8.0, 7.8, 7.7, 7.7, 7.5, 7.5, 7.4,
                   7.4, 7.4, 7.4, 7.3, 7.3, 7.2, 7.2, 7.2, 7.1]

    if sorted_1 == sorted_true:
        print("\nMaxHeap Batch Version: Pass")

    print(sorted_names1)
    print(sorted_1, "\n")


def sort_movies_Incremental_version():
    a_file = open("title.ratings.txt")
    names, ratings = [], []
    next(a_file)
    name_score_dict = {}
    for line in a_file:
        temp = line.rstrip().split('; ')
        names.append(temp[0])  # key: name
        ratings.append(float(temp[1]))  # name: rating
        name_score_dict[temp[0]] = float(temp[1])

    sorted_names2 = sort_movie_incre(names, ratings)

    sorted_2 = []
    for item in sorted_names2:
        sorted_2.append(name_score_dict[item])

    sorted_true = [9.4, 9.3, 9.2, 9.1, 9.0, 9.0, 8.8, 8.8, 8.8, 8.8, 8.7, 8.7,
                   8.6, 8.6, 8.5, 8.5, 8.4, 8.4, 8.4, 8.4, 8.4, 8.4, 8.3, 8.2, 8.1, 8.0, 7.8, 7.7, 7.7, 7.5, 7.5, 7.4,
                   7.4, 7.4, 7.4, 7.3, 7.3, 7.2, 7.2, 7.2, 7.1]

    if sorted_2 == sorted_true:
        print("MaxHeap Incremental Version: Pass")

    print(sorted_names2)
    print(sorted_2, "\n")


def test_heap():
    sort_movies_Batch_version()
    sort_movies_Incremental_version()

    start_Time = time.time()
    sort_movies("title.ratings_1000.txt")
    T1 = (time.time() - start_Time) * 1000
    print(f'RunTime for 1000 Movies: {T1} ms')

    start_Time = time.time()
    sort_movies("title.ratings_10000.txt")
    T2 = (time.time() - start_Time) * 1000
    print(f'RunTime for 10000 Movies: {T2} ms')

    start_Time = time.time()
    sort_movies("title.ratings_100000.txt")
    T3 = (time.time() - start_Time) * 1000
    print(f'RunTime for 100000 Movies: {T3} ms')

    functions = ['1000 Movies', '10000 Movies', '100000 Movies']
    times = [T1, T2, T3]

    plt.figure(figsize=(15, 10))
    plt.bar(functions, times, color=['red', 'green', 'blue'])
    plt.title('Heap Sort execution time comparison for different sample size')
    plt.xlabel('Sample Size')
    plt.ylabel('time in milliseconds')
    plt.show()

    return times
