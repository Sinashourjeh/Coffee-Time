#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

class GeneticAlgorithm {
private:
    std::unordered_map<std::string, int> good_attributes;
    std::unordered_map<std::string, int> bad_attributes;
    int population_size;
    int gene_count;
    int num_generations;
    std::vector<std::vector<std::string>> population;

public:
    GeneticAlgorithm(std::unordered_map<std::string, int> good_attrs, std::unordered_map<std::string, int> bad_attrs,
                     int pop_size, int gene_cnt, int num_gens)
        : good_attributes(good_attrs), bad_attributes(bad_attrs), population_size(pop_size),
          gene_count(gene_cnt), num_generations(num_gens), population({}) {}

    std::vector<std::string> create_chromosome() {
        std::vector<std::string> all_genes;
        for (const auto& entry : good_attributes) all_genes.push_back(entry.first);
        for (const auto& entry : bad_attributes) all_genes.push_back(entry.first);

        std::random_shuffle(all_genes.begin(), all_genes.end());
        std::vector<std::string> chromosome(all_genes.begin(), all_genes.begin() + gene_count);
        return chromosome;
    }

    int fitness(const std::vector<std::string>& chromosome) {
        int score = 0;

        for (const auto& gene : chromosome) {
            if (good_attributes.find(gene) != good_attributes.end()) {
                score += good_attributes.at(gene);
            } else if (bad_attributes.find(gene) != bad_attributes.end()) {
                score += bad_attributes.at(gene);
            }
        }

        return score;
    }

    std::vector<std::vector<std::string>> selection(const std::vector<std::vector<std::string>>& current_population) {
        std::vector<std::vector<std::string>> selected_population = current_population;
        std::sort(selected_population.begin(), selected_population.end(),
                  [&](const std::vector<std::string>& a, const std::vector<std::string>& b) {
                      return fitness(a) > fitness(b);
                  });

        selected_population.resize(static_cast<size_t>(population_size * 0.1));
        return selected_population;
    }

    std::vector<std::string> crossover(const std::vector<std::string>& chromosome1, const std::vector<std::string>& chromosome2) {
        int crossover_point = rand() % (gene_count - 1) + 1;
        std::vector<std::string> first_half(chromosome1.begin(), chromosome1.begin() + crossover_point);
        std::vector<std::string> second_half;

        for (const auto& gene : chromosome2) {
            if (std::find(first_half.begin(), first_half.end(), gene) == first_half.end()) {
                second_half.push_back(gene);
            }
        }

        std::vector<std::string> new_chromosome(first_half.begin(), first_half.end());
        new_chromosome.insert(new_chromosome.end(), second_half.begin(), second_half.end());
        new_chromosome.resize(static_cast<size_t>(gene_count));

        return new_chromosome;
    }

    std::vector<std::string> mutation(const std::vector<std::string>& chromosome) {
        std::vector<std::string> mutated_chromosome = chromosome;
        for (int i = 0; i < static_cast<int>(gene_count * 0.1); ++i) {
            int gene_index = rand() % gene_count;
            std::vector<std::string> all_genes;
            for (const auto& entry : good_attributes) all_genes.push_back(entry.first);
            for (const auto& entry : bad_attributes) all_genes.push_back(entry.first);
            std::vector<std::string> new_genes;

            for (const auto& gene : all_genes) {
                if (std::find(mutated_chromosome.begin(), mutated_chromosome.end(), gene) == mutated_chromosome.end()) {
                    new_genes.push_back(gene);
                }
            }

            mutated_chromosome[gene_index] = new_genes[rand() % new_genes.size()];
        }

        return mutated_chromosome;
    }

    std::vector<std::vector<std::string>> generate_new_generation(const std::vector<std::vector<std::string>>& current_population) {
        std::vector<std::vector<std::string>> new_generation = current_population;
        std::vector<std::vector<std::string>> selected_parents = selection(current_population);

        for (int i = 0; i < static_cast<int>(population_size * 0.1); ++i) {
            std::vector<std::string> parent1 = selected_parents[rand() % selected_parents.size()];
            std::vector<std::string> parent2 = selected_parents[rand() % selected_parents.size()];
            std::vector<std::string> child = crossover(parent1, parent2);
            new_generation.push_back(child);

            for (int j = 0; j < static_cast<int>(population_size * 0.1); ++j) {
                std::vector<std::string> random_chromosome = current_population[rand() % current_population.size()];
                std::vector<std::string> mutated_chromosome = mutation(random_chromosome);
                new_generation.push_back(mutated_chromosome);
            }
        }

        return new_generation;
    }

    void evolve() {
        for (int generation = 0; generation < num_generations; ++generation) {
            population = generate_new_generation(population);
            if ((generation + 1) % 10 == 0) {
                std::cout << "Generation " << generation + 1 << ":\n";
                for (const auto& chromosome : std::vector(population.begin(), population.begin() + static_cast<size_t>(population_size * 0.1))) {
                    std::cout << "Chromosome:";
                    for (const auto& gene : chromosome) {
                        std::cout << " " << gene;
                    }
                    std::cout << "\nFitness Score: " << fitness(chromosome) << "\n\n";
                }
            }
        }

        auto best_chromosome = std::max_element(population.begin(), population.end(),
            [&](const std::vector<std::string>& a, const std::vector<std::string>& b) {
                return fitness(a) < fitness(b);
            });

        std::cout << "Best Chromosome:";
        for (const auto& gene : *best_chromosome) {
            std::cout << " " << gene;
        }
        std::cout << "\nBest Chromosome Score: " << fitness(*best_chromosome) << std::endl;
    }
};

int main() {
    // Define attributes and parameters
    std::unordered_map<std::string, int> good_attributes = {
        {"Honesty", 10},
        {"Perseverance", 9},
        {"Loyalty", 8},
        {"Respect", 7},
        {"Punctual", 6},
        {"Trustworthy", 5}
    };

    std::unordered_map<std::string, int> bad_attributes = {
        {"Lie", -3},
        {"Lazy", -1},
        {"Racism", -2},
        {"Addiction", -4},
        {"SpendThrift", -7},
        {"Deception", -8}
    };

    int population_size = 100;
    int gene_count = 7;
    int num_generations = 50;

    // Create GeneticAlgorithm instance and evolve
    GeneticAlgorithm genetic_algorithm(good_attributes, bad_attributes, population_size, gene_count, num_generations);
    genetic_algorithm.evolve();

    return 0;
}
