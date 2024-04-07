import random

class GeneticAlgorithm:
    def __init__(self, good_attributes, bad_attributes, population_size, gene_count, num_generations):
        self.good_attributes = good_attributes
        self.bad_attributes = bad_attributes
        self.population_size = population_size
        self.gene_count = gene_count
        self.num_generations = num_generations
        self.population = []

    def create_chromosome(self):
        all_genes = list(self.good_attributes.keys()) + list(self.bad_attributes.keys())
        chromosome = random.sample(all_genes, self.gene_count)
        return chromosome

    def fitness(self, chromosome):
        score = 0
        genes = dict()

        for gene in chromosome:
            if gene in self.good_attributes:
                score += self.good_attributes[gene]
                genes[gene] = 1
            elif gene in self.bad_attributes:
                score += self.bad_attributes[gene]
                genes[gene] = -1

        return score + sum(genes.values())

    def selection(self, population):
        population.sort(key=lambda chromosome: self.fitness(chromosome), reverse=True)
        return population[:int(len(population) * 0.1)]

    def crossover(self, chromosome1, chromosome2):
        crossover_point = random.randint(1, self.gene_count - 1)
        first_half = chromosome1[:crossover_point]
        second_half = [gene for gene in chromosome2 if gene not in first_half]
        new_chromosome = first_half + second_half[:self.gene_count - len(first_half)]
        return new_chromosome

    def mutation(self, chromosome):
        mutated_chromosome = chromosome.copy()
        for _ in range(int(len(chromosome) * 0.1)):
            gene_index = random.randint(0, self.gene_count - 1)
            all_genes = list(self.good_attributes.keys()) + list(self.bad_attributes.keys())
            new_genes = [gene for gene in all_genes if gene not in mutated_chromosome]
            mutated_chromosome[gene_index] = random.choice(new_genes)
        return mutated_chromosome

    def generate_new_generation(self):
        new_generation = self.population.copy()
        selected_parents = self.selection(self.population)
        for _ in range(int(self.population_size * 0.1)):
            parent1 = random.choice(selected_parents)
            parent2 = random.choice(selected_parents)
            child = self.crossover(parent1, parent2)
            new_generation.append(child)
            for _ in range(int(self.population_size * 0.1)):
                chromosome = random.choice(self.population)
                mutated_chromosome = self.mutation(chromosome)
                new_generation.append(mutated_chromosome)
        return new_generation

    def evolve(self):
        for generation in range(self.num_generations):
            self.population = self.generate_new_generation()
            if (generation + 1) % 10 == 0:
                print(f"Generation {generation + 1}:")
                for chromosome in self.population[:int(self.population_size * 0.1)]:
                    print("Chromosome:", chromosome)
                    print("Fitness Score:", self.fitness(chromosome))
                    print()

        best_chromosome = max(self.population, key=lambda chromosome: self.fitness(chromosome))
        print("Best Chromosome:", best_chromosome)
        print("Best Chromosome Score:", self.fitness(best_chromosome))


# Define attributes and parameters
good_attributes = {
    'Honesty': 10,
    'Perseverance': 9,
    'Loyalty': 8,
    'Respect': 7,
    'Punctual': 6,
    'Trustworthy': 5
}

bad_attributes = {
    'Lie': -3,
    'Lazy': -1,
    'Racism': -2,
    'Addiction': -4,
    'SpendThrift': -7,
    'Deception': -8
}

population_size = 100
gene_count = 7
num_generations = 50

# Create GeneticAlgorithm instance and evolve
genetic_algorithm = GeneticAlgorithm(good_attributes, bad_attributes, population_size, gene_count, num_generations)
genetic_algorithm.evolve()
