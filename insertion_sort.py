import time

from matplotlib import pyplot as plt


def insertion_sort(filename):
    a_file = open(filename)
    names, ratings = [], []
    next(a_file)
    name_score_dict = {}
    for line in a_file:
        temp = line.rstrip().split('; ')
        names.append(temp[0])  # key: name
        ratings.append(float(temp[1]))  # name: rating
        name_score_dict[temp[0]] = float(temp[1])

    for i in range(1, len(ratings)):
        key_item = ratings[i]
        j = i - 1
        while j >= 0 and ratings[j] > key_item:
            ratings[j + 1] = ratings[j]
            j -= 1
        ratings[j + 1] = key_item
    return ratings


def test_insertion_sort():
    start_Time = time.time()
    insertion_sort("title.ratings_1000.txt")
    T1 = (time.time() - start_Time) * 1000
    print(f'RunTime for 1000 Movies: {T1} ms')

    start_Time = time.time()
    insertion_sort("title.ratings_10000.txt")
    T2 = (time.time() - start_Time) * 1000
    print(f'RunTime for 10000 Movies: {T2} ms')

    start_Time = time.time()
    insertion_sort("title.ratings_100000.txt")
    T3 = (time.time() - start_Time) * 1000
    print(f'RunTime for 100000 Movies: {T3} ms')

    functions = ['1000 Movies', '10000 Movies', '100000 Movies']
    times = [T1, T2, T3]

    plt.figure(figsize=(15, 10))
    plt.bar(functions, times, color=['red', 'green', 'blue'])
    plt.title("Insertion Sort execution time comparison for different sample size")
    plt.xlabel('Sample Size')
    plt.ylabel('time in milliseconds')
    plt.show()

    return times
