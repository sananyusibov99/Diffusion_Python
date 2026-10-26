# Diffusion simulation (Python)

A Monte Carlo model of particle diffusion in one and two dimensions. This was homework for the *Computer Sciences for Physics and Chemistry* course at UFAZ (December 2019).

## Part 1. Random walk in 1D: `Homework.py`

A "drunk walker" takes N steps along a line, moving forward with probability *p* and backward with probability 1 − *p*.

- 100 runs each for 20, 50, 100, 200 and 1000 steps at *p* = 0.5
- A histogram of final positions with a fitted curve, showing the distribution is close to normal
- The standard deviation σ for each N, and a plot of σ(N), which grows like √N
- The same experiment at *p* = 0.75, where the walker drifts forward

## Part 2. Dye diffusion in 2D: `Homework2.py`

100 dye particles start in the four centre cells of a 20 × 20 grid. At each step a particle stays put with probability *p* = 0.2; otherwise it moves to a neighbouring cell. All directions are equally likely, and the particle cannot leave the grid. Cells in corners and on edges are handled separately.

- Scatter plots of particle positions at the start and after 5, 10, 20 and 50 steps
- Entropy of the system, S = −k_B · Σ Pᵢ · ln Pᵢ, averaged over 25 runs, for 5 to 200 steps
- A plot of entropy against the number of steps, which shows it rising as the particles spread out

## Tech stack

Python, NumPy, SciPy, Matplotlib, Seaborn

## How to run

```bash
pip install numpy scipy matplotlib seaborn
python Homework.py
python Homework2.py
```

Each script opens its plots one after another.
