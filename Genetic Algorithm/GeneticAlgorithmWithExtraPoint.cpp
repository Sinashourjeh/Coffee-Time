#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cstdlib>
#include <ctime>

class GeneticAlgorithm {
public:
    GeneticAlgorithm(const std::unordered_map<std::string, int>& goodAttributes,
                     const std::unordered_map<std::string, int>& badAttributes,
                     int populationSize, int geneCount, int numGenerations)
        : goodAttributes(goodAttributes),
          badAttributes(badAttributes),
          populationSize(populationSize),
          geneCount(geneCount),
          numGenerations(numGenerations),
          population() {}

    std::vector<std::string> createChromosome() {
        std::vector<std::string> chromosome;
        std::vector<std::string> allGenes;

        for (const auto& entry : goodAttributes) {
            allGenes.push_back(entry.first);
        }

        for (const auto& entry : badAttributes) {
            allGenes.push_back(entry.first);
        }

        std::random_shuffle(allGenes.begin(), allGenes.end());

        for (int i = 0; i < geneCount; ++i) {
            chromosome.push_back(allGenes[i]);
        }

        return chromosome;
    }

    int fitness(const std::vector<std::string>& chromosome) {
        int score = 0;
        std::unordered_map<std::string, int> genes;

        for (const auto& gene : chromosome) {
            if (goodAttributes.find(gene) != goodAttributes.end()) {
                score += goodAttributes.at(gene);
                genes[gene] = 1;
            } else if (badAttributes.find(gene) != badAttributes.end()) {
                score += badAttributes.at(gene);
                genes[gene] = -1;
            }
        }

        return score + std::accumulate(genes.begin(), genes.end(), 0,
            [](int acc, const auto& entry) { return acc + entry.second; });
    }

    std::vector<std::vector<std::string>> selection(const std::vector<std::vector<std::string>>& population) {
        std::vector<std::vector<std::string>> sortedPopulation = population;
        std::sort(sortedPopulation.begin(), sortedPopulation.end(),
                  [this](const auto& chromo1, const auto& chromo2) {
                      return this->fitness(chromo1) > this->fitness(chromo2);
                  });

        int selectedSize = static_cast<int>(populationSize * 0.1);
        return std::vector<std::vector<std::string>>(sortedPopulation.begin(), sortedPopulation.begin() + selectedSize);
    }

    std::vector<std::string> crossover(const std::vector<std::string>& chromosome1,
                                       const std::vector<std::string>& chromosome2) {
        int crossoverPoint = rand() % (geneCount - 1) + 1;
        std::vector<std::string> firstHalf(chromosome1.begin(), chromosome1.begin() + crossoverPoint);

        std::vector<std::string> secondHalf;
        std::copy_if(chromosome2.begin(), chromosome2.end(), std::back_inserter(secondHalf),
                     [&firstHalf](const auto& gene) {
                         return std::find(firstHalf.begin(), firstHalf.end(), gene) == firstHalf.end();
                     });

        std::vector<std::string> newChromosome(firstHalf.begin(), firstHalf.end());
        newChromosome.insert(newChromosome.end(), secondHalf.begin(), secondHalf.end());

        return std::vector<std::string>(newChromosome.begin(), newChromosome.begin() + geneCount);
    }

    std::vector<std::string> mutation(const std::vector<std::string>& chromosome) {
        std::vector<std::string> mutatedChromosome = chromosome;

        for (int i = 0; i < static_cast<int>(geneCount * 0.1); ++i) {
            int geneIndex = rand() % geneCount;
            std::vector<std::string> allGenes;

            for (const auto& entry : goodAttributes) {
                allGenes.push_back(entry.first);
            }

            for (const auto& entry : badAttributes) {
                allGenes.push_back(entry.first);
            }

            std::vector<std::string> newGenes;
            std::copy_if(allGenes.begin(), allGenes.end(), std::back_inserter(newGenes),
                         [&mutatedChromosome](const auto& gene) {
                             return std::find(mutatedChromosome.begin(), mutatedChromosome.end(), gene) == mutatedChromosome.end();
                         });

            mutatedChromosome[geneIndex] = newGenes[rand() % newGenes.size()];
        }

        return mutatedChromosome;
    }

    std::vector<std::vector<std::string>> generateNewGeneration() {
        std::vector<std::vector<std::string>> newGeneration = population;
        std::vector<std::vector<std::string>> selectedParents = selection(population);

        for (int i = 0; i < static_cast<int>(populationSize * 0.1); ++i) {
            std::vector<std::string> parent1 = selectedParents[rand() % selectedParents.size()];
            std::vector<std::string> parent2 = selectedParents[rand() % selectedParents.size()];
            std::vector<std::string> child = crossover(parent1, parent2);
            newGeneration.push_back(child);

            for (int j = 0; j < static_cast<int>(populationSize * 0.1); ++j) {
                std::vector<std::string> randomChromosome = population[rand() % population.size()];
                std::vector<std::string> mutatedChromosome = mutation(randomChromosome);
                newGeneration.push_back(mutatedChromosome);
            }
        }

        return newGeneration;
    }

    void evolve() {
        for (int generation = 0; generation < numGenerations; ++generation) {
            population = generateNewGeneration();

            if ((generation + 1) % 10 == 0) {
                std::cout << "Generation " << generation + 1 << ":" << std::endl;
                for (const auto& chromosome : std::vector<std::vector<std::string>>(population.begin(), population.begin() + static_cast<int>(populationSize * 0.1))) {
                    std::cout << "Chromosome: ";
                    for (const auto& gene : chromosome) {
                        std::cout << gene << " ";
                    }
                    std::cout << std::endl;
                    std::cout << "Fitness Score: " << fitness(chromosome) << std::endl << std::endl;
                }
            }
        }

        auto bestChromosome = std::max_element(population.begin(), population.end(),
            [this](const auto& chromo1, const auto& chromo2) {
                return this->fitness(chromo1) < this->fitness(chromo2);
            });

        std::cout << "Best Chromosome: ";
        for (const auto& gene : *bestChromosome) {
            std::cout << gene << " ";
        }
        std::cout << std::endl;

        std::cout << "Best Chromosome Score: " << fitness(*bestChromosome) << std::endl;
    }

private:
    std::unordered_map<std::string, int> goodAttributes;
    std::unordered_map<std::string, int> badAttributes;
    int populationSize;
    int geneCount;
    int numGenerations;
    std::vector<std::vector<std::string>> population;
};

int main() {
    std::unordered_map<std::string, int> goodAttributes = {
        {"Honesty", 10},
        {"Perseverance", 9},
        {"Loyalty", 8},
        {"Respect", 7},
        {"Punctual", 6},
        {"Trustworthy", 5}
    };

    std::unordered_map<std::string, int> badAttributes = {
        {"Lie", -3},
        {"Lazy", -1},
        {"Racism", -2},
        {"Addiction", -4},
        {"SpendThrift", -7},
        {"Deception", -8}
    };

    int populationSize = 100;
    int geneCount = 7;
    int numGenerations = 50;

    srand(static_cast<unsigned>(time(0)));

    GeneticAlgorithm geneticAlgorithm(goodAttributes, badAttributes, populationSize, geneCount, numGenerations);
    geneticAlgorithm.evolve();

    return 0;
}
