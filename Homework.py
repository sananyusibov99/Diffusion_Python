import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import requests
import seaborn as sns
import random

sns.set(color_codes=True)

sigma = 0.1
mu = 0.5

p = 0.5  # Probability
Prob_Forward = p
Prob_Back = 1 - p
position = 0
answers = list()
standard_dev = list()
steps_all = [20, 50, 100, 200, 1000]


def func(position,times, steps):
    for y in range(times):
        for x in range(steps):
            prob = random.random()
            if prob <= Prob_Forward:
                position += 1
            else:
                position -= 1
        answers.append(position)
        position=0

def show_hist(times, steps):
    # Result as histogram
    sns.distplot(answers, kde=False, rug=True)
    plt.title(f"{times} times - {steps} steps")
    plt.show()

    # Calculate standard deviation
    std = np.std(answers)
    print(f"Standard deviation for {steps} steps - {std}")
    standard_dev.append(std)
    # Demonstrate that distribution is Gaussian
    sns.distplot(answers, rug=True)
    plt.title(f"{times} times - {steps} steps with Distribution curve")
    plt.show()

times=100

# Running function 100 times for 20 steps.
answers.clear()
steps=20
func(position,times, steps)
# Show histograms
show_hist(times, steps)

# Running function 100 times for 50 steps.
answers.clear()
steps=50
func(position,times, steps)
# Show histograms
show_hist(times, steps)

# Running function 100 times for 100 steps.
answers.clear()
steps=100
func(position,times, steps)
# Show histograms
show_hist(times, steps)

# Running function 100 times for 200 steps.
answers.clear()
steps=200
func(position,times, steps)
# Show histograms
show_hist(times, steps)

# Running function 100 times for 1000 steps.
answers.clear()
steps=1000
func(position,times, steps)
# Show histograms
show_hist(times, steps)

print(steps_all)
print(standard_dev)
plt.plot(steps_all, standard_dev)
plt.xlabel('Steps')
plt.ylabel('Standard deviation')
plt.show()


# Running function 100 times for 1000 steps with prob 0.75.
p=0.75
Prob_Forward = p
Prob_Back = 1 - p
position = 0
answers.clear()
times=100
steps=1000
func(position,times, steps)
# Show histograms
show_hist(times, steps)