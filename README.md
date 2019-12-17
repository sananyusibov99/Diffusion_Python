# Diffusion_Python
Computer Sciences for Physics and Chemistry – Homework
This exercise is about the modeling of the diffusion of particles in physics or chemistry. It is composed of two parts, one simulating the diffusion in one dimension and one in a plane.

**First part**
**Diffusion in 1 dimension: the drunk walker**

Let us consider a drunk walker that moves along in a street (considered as a straight line). At each step, he has a probability 𝑝 to move forward and 1 − 𝑝 to move backward.
1. Write a function that calculates the final position of the walker as a function of the parameter 𝑝 and the number of steps 𝑁.
2. What is the expected final position for 𝑝 = 0.5? Check your guess by running your function 100 times for 1000 steps.
3. Represent the result as a histogram. Calculate the standard deviation 𝜎1000 and demonstrate that the distribution you obtained is a Gaussian.
4. Do the same for 20, 50, 100 and 200 steps. Fit the standard deviation 𝜎𝑁 as a function of the number of steps 𝑁 with appropriate mathematical law.
5. Now 𝑝 = 0.75. What is the expected final position as a function of the number of time steps N. Check your assumption.

**Second part**
**Diffusion in 2 dimensions: diffusion of a dye in water**

In this part, we will simulate the diffusion of a dye drop in a water puddle. The water puddle is represented by a lattice of 20 lines and 20 columns. At the initial time step, box of the lattice is empty, except the four at the center which contains 100 particles of dye. At each time step, each molecule moves according to the following rules :
(i) the molecule has a probability 𝑝 to stay in its box,
(ii) if the molecule moves, it moves one box and all possible moving directions are
equiprobable (e.g. 0.25 ∙ (1 − 𝑝) to go up, down, left or right if the particle is in the center of the lattice, 0.33 ∙ (1 − 𝑝) to go up, down or left if the particle in is a top-right box of a row, or 0.5 ∙ (1 − 𝑝) to go down or right if the particle is in the upper left corner box), and
(iii) the molecule can not go out of the lattice.
 
1. Write a function that computes the final position of each molecule walker as a function of the parameter 𝑝 and the number of steps 𝑁.
2. Fix 𝑝 = 0.2. Represent the positions of the molecules in a scattered plot after 5, 10, 20 and 50 time steps.
In physics or chemistry, we define the notion of entropy to quantify the neatness of a system. For a discrete system, the entropy is calculated like this
𝑆=−𝑘𝐵 ∙∑𝑃𝑖 ∙𝑙𝑛(𝑃𝑖)
Where 𝑘𝐵 = 1.38𝑒−23 is the Boltzmann constant and 𝑃𝑖 is the average ratio of particles in the box 𝑖 (number of particle in the box 𝑖 divided by the total number of particle
3. Run 25 computations with 𝑵 = 𝟓𝟎 time steps and calculate the average value of 𝑃𝑖 for each box. Then, computes the entropy for 𝑵 = 𝟓𝟎.
4. Do the same for 𝑵=𝟓, 𝑵=𝟏𝟎, 𝑵=𝟐𝟎 and 𝑵=𝟓𝟎. Plot S(N) and find a mathematical function that fits the variation of entropy with respect to the number of time steps S(N)
