import time
from random import randint

from matplotlib import pyplot as plt


def quick_sort_filename(filename):
    a_file = open(filename)
    names, ratings = [], []
    next(a_file)
    name_score_dict = {}
    for line in a_file:
        temp = line.rstrip().split('; ')
        names.append(temp[0])  # key: name
        ratings.append(float(temp[1]))  # name: rating
        name_score_dict[temp[0]] = float(temp[1])

    if len(ratings) < 2:
        return ratings

    low, same, high = [], [], []

    pivot = ratings[randint(0, len(ratings) - 1)]

    for item in ratings:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quick_sort(low) + same + quick_sort(high)


def quick_sort(ratings):
    if len(ratings) < 2:
        return ratings

    low, same, high = [], [], []

    pivot = ratings[randint(0, len(ratings) - 1)]

    for item in ratings:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quick_sort(low) + same + quick_sort(high)


def test_quick_sort():
    start_Time = time.time()
    quick_sort_filename("title.ratings_1000.txt")
    T1 = (time.time() - start_Time) * 1000
    print(f'RunTime for 1000 Movies: {T1} ms')

    start_Time = time.time()
    quick_sort_filename("title.ratings_10000.txt")
    T2 = (time.time() - start_Time) * 1000
    print(f'RunTime for 10000 Movies: {T2} ms')

    start_Time = time.time()
    quick_sort_filename("title.ratings_100000.txt")
    T3 = (time.time() - start_Time) * 1000
    print(f'RunTime for 100000 Movies: {T3} ms')

    functions = ['1000 Movies', '10000 Movies', '100000 Movies']
    times = [T1, T2, T3]

    plt.figure(figsize=(15, 10))
    plt.bar(functions, times, color=['red', 'green', 'blue'])
    plt.title('Quick Sort execution time comparison for different sample size')
    plt.xlabel('Sample Size')
    plt.ylabel('time in milliseconds')
    plt.show()

    return times
