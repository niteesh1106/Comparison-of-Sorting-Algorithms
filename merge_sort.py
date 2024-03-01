import time

from matplotlib import pyplot as plt


def merge_sort_filename(filename):
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

    midpoint = len(ratings) // 2

    return merge(
        left=merge_sort(ratings[:midpoint]),
        right=merge_sort(ratings[midpoint:]))


def merge_sort(ratings):
    if len(ratings) < 2:
        return ratings

    midpoint = len(ratings) // 2

    return merge(
        left=merge_sort(ratings[:midpoint]),
        right=merge_sort(ratings[midpoint:]))


def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def test_merge_sort():
    start_Time = time.time()
    merge_sort_filename("title.ratings_1000.txt")
    T1 = (time.time() - start_Time) * 1000
    print(f'RunTime for 1000 Movies: {T1} ms')

    start_Time = time.time()
    merge_sort_filename("title.ratings_10000.txt")
    T2 = (time.time() - start_Time) * 1000
    print(f'RunTime for 10000 Movies: {T2} ms')

    start_Time = time.time()
    merge_sort_filename("title.ratings_100000.txt")
    T3 = (time.time() - start_Time) * 1000
    print(f'RunTime for 100000 Movies: {T3} ms')

    functions = ['1000 Movies', '10000 Movies', '100000 Movies']
    times = [T1, T2, T3]

    plt.figure(figsize=(15, 10))
    plt.bar(functions, times, color=['red', 'green', 'blue'])
    plt.title('Merge Sort execution time comparison for different sample size')
    plt.xlabel('Sample Size')
    plt.ylabel('time in milliseconds')
    plt.show()

    return times
