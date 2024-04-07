# Genetic Algorithm with Mutation and Crossover for New Generation Generation

This project implements a genetic algorithm in both Python and C++ to generate a new generation of solutions through a combination of mutation and crossover operations. Genetic algorithms are a powerful optimization technique inspired by the process of natural selection, allowing for the evolution of potential solutions to a problem over multiple generations.

## Table of Contents

- [Introduction](#introduction)
- [Algorithm Overview](#algorithm-overview)
- [Components](#components)
  - [Chromosome Representation](#chromosome-representation)
  - [Fitness Function](#fitness-function)
  - [Selection](#selection)
  - [Crossover](#crossover)
  - [Mutation](#mutation)
  - [Termination Condition](#termination-condition)
- [Usage](#usage)
  - [Python Implementation](#python-implementation)
  - [C++ Implementation](#cpp-implementation)
- [Contributing](#contributing)
- [License](#license)
- [Developers](#developers)
- [System & Hardware](#system--hardware)

## Introduction

Genetic algorithms are a subset of evolutionary algorithms that mimic the process of natural selection to evolve potential solutions to optimization and search problems. This project focuses on implementing a genetic algorithm with mutation and crossover functions to create a new generation of solutions iteratively.

## Algorithm Overview

1. **Initialization:** A population of potential solutions (chromosomes) is created randomly.

2. **Evaluation:** Each chromosome's fitness is evaluated using a user-defined fitness function that quantifies how well the chromosome solves the problem.

3. **Selection:** A subset of chromosomes is selected for reproduction based on their fitness. This subset is more likely to contain chromosomes that have higher fitness scores.

4. **Crossover:** Pairs of selected chromosomes undergo crossover, producing offspring with characteristics inherited from both parents.

5. **Mutation:** Some of the offspring's genes are subject to mutation, introducing small, random changes to diversify the population.

6. **Termination:** The process continues for a predetermined number of generations or until a termination condition is met (e.g., satisfactory solution found).

## How does it work

Here are detailed comments for each function in the provided Python code:

```python
# Import necessary libraries
import random

# Function to create a random chromosome
def create_chromosome():
    all_genes = list(good_attributes.keys()) + list(bad_attributes.keys())
    chromosome = random.sample(all_genes, gene_count)
    return chromosome

# Function to calculate the fitness score of a chromosome
def fitness(chromosome):
    score = 0
    for gene in chromosome:
        if gene in good_attributes:
            score += good_attributes[gene]
        elif gene in bad_attributes:
            score += bad_attributes[gene]
    return score

# Function for selection of top-performing chromosomes
def selection(population):
    population.sort(key=lambda chromosome: fitness(chromosome), reverse=True)
    return population[:int(len(population) * 0.1)]

# Function for crossover between two parent chromosomes
def crossover(chromosome1, chromosome2):
    crossover_point = random.randint(1, gene_count - 1)
    first_half = chromosome1[:crossover_point]
    second_half = [gene for gene in chromosome2 if gene not in first_half]
    new_chromosome = first_half + second_half[:gene_count - len(first_half)]
    return new_chromosome

# Function for introducing mutation in a chromosome
def mutation(chromosome):
    mutated_chromosome = chromosome.copy()
    for _ in range(int(len(chromosome) * 0.1)):
        gene_index = random.randint(0, gene_count - 1)
        all_genes = list(good_attributes.keys()) + list(bad_attributes.keys())
        new_genes = [gene for gene in all_genes if gene not in mutated_chromosome]
        mutated_chromosome[gene_index] = random.choice(new_genes)
    return mutated_chromosome

# Function to generate a new generation
def generate_new_generation(population):
    new_generation = population.copy()
    selected_parents = selection(population)
    for _ in range(int(population_size * 0.1)):
        parent1 = random.choice(selected_parents)
        parent2 = random.choice(selected_parents)
        child = crossover(parent1, parent2)
        new_generation.append(child)
        for _ in range(int(population_size * 0.1)):
            chromosome = random.choice(population)
            mutated_chromosome = mutation(chromosome)
            new_generation.append(mutated_chromosome)
    return new_generation
```

```python
# Number of generations to run the algorithm
num_generations = 50

# Main loop for running the genetic algorithm
for generation in range(num_generations):
    population = generate_new_generation(population)
    if (generation + 1) % 10 == 0:
        print(f"Generation {generation + 1}:")
        for chromosome in population[:int(population_size * 0.1)]:
            print("Chromosome:", chromosome)
            print("Fitness Score:", fitness(chromosome))
            print()

# Identify the best chromosome from the final population
best_chromosome = max(population, key=lambda chromosome: fitness(chromosome))

# Print the best chromosome and its fitness score
print("Best Chromosome:", best_chromosome)
print("Best Chromosome Score:", fitness(best_chromosome))
```

This code runs the genetic algorithm for a specified number of generations, updating the population by generating a new generation in each iteration. It prints the chromosomes and their fitness scores for every 10th generation and identifies the best chromosome based on the highest fitness score.

## Components

### Chromosome Representation

Chromosomes are represented as data structures containing genetic information. The structure of chromosomes should be defined based on the problem domain. For example, in a binary optimization problem, chromosomes can be represented as strings of 0s and 1s.

### Fitness Function

The fitness function quantifies the quality of a solution. It takes a chromosome as input and returns a fitness score that indicates how well the chromosome solves the problem. Higher fitness scores correspond to better solutions.

### Selection

Various selection strategies can be employed to choose chromosomes for reproduction. Common methods include tournament selection, roulette wheel selection, and rank-based selection.

### Crossover

Crossover involves combining genetic information from two parent chromosomes to produce one or more offspring. Different crossover techniques, such as one-point, two-point, or uniform crossover, can be applied based on the problem characteristics.

### Mutation

Mutation introduces small, random changes to individual genes within chromosomes. This helps maintain diversity in the population and prevents convergence to local optima.

### Termination Condition

The algorithm terminates when a specific condition is met, such as reaching a maximum number of generations or achieving a satisfactory solution.

## Usage

### Python Implementation

1. Install the required dependencies by running: `pip install numpy`

2. Run the Python script: `GeneticAlgorithmWithRealPoint.py` or `GeneticAlgorithmWithExtraPoint.py`

3. Follow the on-screen instructions to provide necessary inputs and parameters.

### C++ Implementation

1. Compile the C++ code: `g++ -o GeneticAlgorithmWithRealPoint.cpp` or `g++ -o GeneticAlgorithmWithExtraPoint.cpp`

2. Run the compiled executable: `./GeneticAlgorithm`

3. Follow the prompts to input required parameters.

## Contributing

This is an open-source project, and contributions are welcome. To contribute,

 please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Developers

<p align="center">
<a href="https://github.com/Awrsha"><img src="https://avatars.githubusercontent.com/u/89135083?v=4" width="100;" alt="Awrsha Parvizi"/><br /><sub><b>.:: Amir M. Parvizi ::.</b></sub></a>
</p>

<p align="center">
<a href="https://github.com/ali-hamidi2000"><img src="https://avatars.githubusercontent.com/u/140819925?v=4" width="100;" alt="Ali hamidi"/><br /><sub><b>.:: Ali hamidi ::.</b></sub></a>
</p>

## System & Hardware

### ⚙️ Things I use to get stuff done
- **OS:** Windows 11
- **Laptop:** TUF Gaming
- **Code Editor:** Visual Studio Code - The best editor out there.
- **To Stay Updated:** Medium, Linkedin, and Instagram.
- ⚛️ [Checkout Our VSCode Configurations Here](#) 

💙 If you like my projects, Give them ⭐ and Share it with friends!


<p align="center">
<img src="https://raw.githubusercontent.com/mayhemantt/mayhemantt/Update/svg/Bottom.svg" alt="Github Stats" />
</p>
