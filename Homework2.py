import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
from scipy import optimize

import math

matrix = []
field = []
row = []
number = 0
entropy = []
steps = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 200]

probability_stay = 0.2
probability_corner = 0.5 * (1 - probability_stay)
probability_middle = 0.25 * (1 - probability_stay)
probability_edge = 0.33 * (1 - probability_stay)
print(f"probability_corner: {probability_corner}")
print(f"probability_middle: {probability_middle}")
print(f"probability_edge: {probability_edge}")


def cleaning(matrix, field, number):
    matrix.clear()
    field.clear()
    number = 0


def create_array_points():
    for i in range(100):
        row = []
        for j in range(2):
            row.append(0)
        matrix.append(row)


def create_array_field():
    for i in range(600):
        row = []
        for j in range(1):
            row.append(0)
        field.append(row)


def fill_array_points():
    for i in matrix:
        i[0] = random.randint(10, 11)
        i[1] = random.randint(10, 11)


def fill_array_field(matrix, field):
    for i in matrix:
        x = i[0]
        y = i[1]
        # print(field[x*20+y][0])
        field[x * 20 + y][0] += 1


def print_array_points(number):
    for i in matrix:
        number += 1
        if number % 10 == 0:
            print(i)
        else:
            print(i, end=" ")


def print_array_field(number):
    for i in field:
        number += 1
        if number % 20 == 0:
            print(i)
        else:
            print(i, end=" ")


def show_matrix_in_graph(name_of_graph):
    for i in matrix:
        plt.scatter(i[0], i[1], color="blue")
    # locs, labels = xticks()
    plt.axis("square")
    plt.xticks(np.arange(0, 21, step=1))
    plt.yticks(np.arange(0, 21, step=1))
    plt.grid(color='grey', linestyle='-', linewidth=1, alpha=0.2)
    plt.title(name_of_graph)
    plt.show()


def move_points():
    random_number = 0
    for i in matrix:
        random_number = random.random()
        random_number2 = random.random()

        # Corners
        if i[0] == 0 and i[1] == 20:
            if random_number <= probability_stay:
                continue
            elif random_number <= probability_stay + probability_corner:
                i[0] += 1
            else:
                i[1] -= 1
        elif i[0] == 20 and i[1] == 0:
            if random_number <= probability_stay:
                continue
            elif random_number <= probability_stay + probability_corner:
                i[0] -= 1
            else:
                i[1] += 1
        elif i[0] == 0 and i[1] == 0:
            if random_number <= probability_stay:
                continue
            elif random_number <= probability_stay + probability_corner:
                i[0] += 1
            else:
                i[1] += 1
        elif i[0] == 20 and i[1] == 20:
            if random_number <= probability_stay:
                continue
            elif random_number <= probability_stay + probability_corner:
                i[0] -= 1
            else:
                i[1] -= 1
        # Edges
        elif i[0] == 0 and i[1] != 0 and i[1] != 20:
            if random_number <= probability_stay:
                continue
            elif random_number <= probability_stay + probability_edge:
                i[0] += 1
            elif random_number <= probability_stay + probability_edge + probability_edge:
                i[1] -= 1
            else:
                i[1] += 1
        elif i[0] == 20 and i[1] != 0 and i[1] != 20:
            if random_number <= probability_stay:
                continue
            elif random_number <= probability_stay + probability_edge:
                i[0] -= 1
            elif random_number <= probability_stay + probability_edge + probability_edge:
                i[1] += 1
            else:
                i[1] -= 1
        elif i[1] == 0 and i[0] != 0 and i[0] != 20:
            if random_number <= probability_stay:
                continue
            elif random_number <= probability_stay + probability_edge:
                i[0] += 1
            elif random_number <= probability_stay + probability_edge + probability_edge:
                i[0] -= 1
            else:
                i[1] += 1
        elif i[1] == 20 and i[0] != 0 and i[0] != 20:
            if random_number <= probability_stay:
                continue
            elif random_number <= probability_stay + probability_edge:
                i[0] += 1
            elif random_number <= probability_stay + probability_edge + probability_edge:
                i[0] -= 1
            else:
                i[1] -= 1
        # Center
        elif i[0] != 0 and i[0] != 20 and i[1] != 0 and i[1] != 20:
            if random_number <= probability_stay:
                continue
            elif random_number <= probability_stay + probability_middle:
                i[0] += 1
            elif random_number <= probability_stay + 2 * probability_middle:
                i[0] -= 1
            elif random_number <= probability_stay + 3 * probability_middle:
                i[1] += 1
            else:
                i[1] -= 1


def computations(steps):
    cleaning(matrix, field, number)
    create_array_points()
    create_array_field()
    fill_array_points()
    # print_array_points(number=0)
    for j in range(25):
        for i in range(steps):
            move_points()
        fill_array_field(matrix, field)
        matrix.clear()
        create_array_points()
        fill_array_points()

    # print_array_field(number=0)
    for i in field:
        i[0] /= 100
        i[0] /= 25
    # print_array_field(number=0)

    empty = 0
    s = 0
    Summation = 0
    for i in field:
        try:
            Summation += math.log(i[0]) * i[0]
        except:
            empty += 1

    s = -const.Boltzmann * Summation
    print(f"25 iterations - {steps} steps, entropy is {s}")
    entropy.append(s)


create_array_points()
fill_array_points()
print_array_points(number=0)

show_matrix_in_graph("Before")

# 5 Steps
for i in range(5):
    move_points()
show_matrix_in_graph("5 Steps")

# 10 Steps
for i in range(5):
    move_points()
show_matrix_in_graph("10 Steps")

# 20 Steps
for i in range(10):
    move_points()
show_matrix_in_graph("20 Steps")

# 50 Steps
for i in range(30):
    move_points()
show_matrix_in_graph("50 Steps")

create_array_field()
# print_array_field(number=0)
fill_array_field(matrix, field)
# print_array_field(number=0)

# Calculation of number of points to check if it is correct
# sum=0
# for i in field:
#  sum += i[0]
# print(sum)

computations(steps=5)
computations(steps=10)
computations(steps=15)
computations(steps=20)
computations(steps=25)
computations(steps=30)
computations(steps=35)
computations(steps=40)
computations(steps=45)
computations(steps=50)
computations(steps=55)
computations(steps=60)
computations(steps=65)
computations(steps=70)
computations(steps=75)
computations(steps=80)
computations(steps=85)
computations(steps=90)
computations(steps=95)
computations(steps=100)
computations(steps=200)

plt.plot(steps, entropy)

plt.xlabel("Steps")
plt.ylabel("Entropy")

plt.show()
