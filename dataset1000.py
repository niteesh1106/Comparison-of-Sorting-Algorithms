"""import string
import random
import time

from heap import *

if __name__ == "__main__":
    with open("title.ratings_1000.txt", 'w') as a_file1:
        for line in range(0,1000):
            movie = ''.join(random.choice(string.ascii_letters) for i in range(10))
            rating = str(round(random.uniform(1,10),1))
            a_file1.write(movie)
            a_file1.write(" ; ")
            a_file1.write(rating)
            a_file1.write("\n")

    a_file2 = open("title.ratings_1000.txt")
    names1000, ratings1000 = [], []
    next(a_file2)
    name_score_dict1000 = {}
    for line in a_file1:
        temp = line.rstrip().split(" ; ")
        names1000.append(temp[0])  # key: name
        ratings1000.append(float(temp[1]))  # name: rating
        name_score_dict1000[temp[0]] = float(temp[1])

    print(name_score_dict1000)
    sorted_names1 = sort_movies_batch(names1000, ratings1000)

    sorted_1 = []
    for item in sorted_names1:
        sorted_1.append(name_score_dict1000[item])

    print("Movies to Watch on Fridays!\n")
    i = 0
    for item in sorted_names1:
        print(item + " : " + str(sorted_1[i]))
        i += 1


    with open("title.ratings_100000.txt", 'w') as a_file1:
        for line in range(0,100000):
            movie = ''.join(random.choice(string.ascii_letters) for i in range(10))
            rating = str(round(random.uniform(1,10),1))
            a_file1.write(movie)
            a_file1.write(" ; ")
            a_file1.write(rating)
            a_file1.write("\n")

    a_file1 = open("title.ratings_100000.txt")
    names1000, ratings1000 = [], []
    next(a_file1)
    name_score_dict1000 = {}
    for line in a_file1:
        temp = line.rstrip().split('; ')
        names1000.append(temp[0])  # key: name
        ratings1000.append(float(temp[1]))  # name: rating
        name_score_dict1000[temp[0]] = float(temp[1])

    sorted_names1 = sort_movies_batch(names1000, ratings1000)







      print("Movies to Watch on Fridays!\n")
    i = 0
    for item in sorted_names2:
        print(item + " : " + str(sorted_2[i]))
        i += 1



import string
import random
import time
import matplotlib.pyplot as plt

from heap import *

if __name__ == "__main__":

    start_Time1 = time.time() * 1000
    print("Start Time: " + str(start_Time1))

    a_file = open("title.ratings_100000.txt")
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
        print("Heap Batch sorting pass\n")

    sorted_names2 = sort_movie_incre(names, ratings)

    sorted_2 = []
    for item in sorted_names2:
        sorted_2.append(name_score_dict[item])

    if sorted_2 == sorted_true:
        print("Heap Incremental sorting pass\n")

    print("Movies to Watch on Fridays!\n")
    i = 0
    for item in sorted_names2:
        print(item + " : " + str(sorted_2[i]))
        i += 1

    end_Time1 = time.time() * 1000
    print("end Time: " + str(end_Time1))

    total_Time1 = end_Time1 - start_Time1
    print("RunTime: " + str(total_Time1))

    plt.rcParams




start_Time = time.time()
bubble_sort("title.ratings_100000.txt")
T4 = (time.time() - start_Time) * 1000
print(f'RunTime for 1000 Movies: {T4} ms') """