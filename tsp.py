import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt
from models.fitness import Fitness

# Create our initial population
# Route generator
# This method randomizes the order of the cities, this mean that this method creates a random individual.
from models.responseTsp import ResponseTsp


def create_route(district_list):
    route = random.sample(district_list, len(district_list))
    return route


# Create first "population" (list of routes)
# This method created a random population of the specified size.

def initial_population(popSize, district_list):
    population = []

    for i in range(0, popSize):
        population.append(create_route(district_list))
    return population

# Create the genetic algorithm
# Rank individuals
# This function takes a population and orders it in descending order using the fitness of each individual
def rank_routes(population):
    fitness_results = {}
    for i in range(0, len(population)):
        fitness_results[i] = Fitness(population[i]).route_fitness()
    sorted_results = sorted(fitness_results.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_results


# Create a selection function that will be used to make the list of parent routes

def selection(popRanked, eliteSize):
    selection_results = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()

    for i in range(0, eliteSize):
        selection_results.append(popRanked[i][0])

    #print(selection_results);
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100 * random.random()
        for j in range(0, len(popRanked)):
            if pick <= df.iat[j, 3]:
                selection_results.append(popRanked[j][0])
                break
    return selection_results


# Create mating pool

def mating_pool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool


# Create a crossover function for two parents to create one child
def breed(parent1, parent2):
    child = []
    child_p1 = []
    child_p2 = []

    gene_a = int(random.random() * len(parent1))
    gene_b = int(random.random() * len(parent1))

    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)

    for i in range(start_gene, end_gene):
        child_p1.append(parent1[i])

    child_p2 = [item for item in parent2 if item not in child_p1]
    #print(startGene, endGene)

    #print(parent1)
    #print(parent2)

    #print(childP1)
    #print(childP2)
    child = child_p1 + child_p2

    #print(child)
    return child


# Create function to run crossover over full mating pool

def breed_population(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, eliteSize):
        children.append(matingpool[i])

    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool) - i - 1])
        children.append(child)
    return children


# Create function to mutate a single route
def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if random.random() < mutationRate:
            swap_with = int(random.random() * len(individual))

            district1 = individual[swapped]
            district2 = individual[swap_with]

            individual[swapped] = district1
            individual[swap_with] = district2
    return individual


# Create function to run mutation over entire population

def mutate_population(population, mutationRate):
    mutated_pop = []

    for ind in range(0, len(population)):
        mutated_ind = mutate(population[ind], mutationRate)
        mutated_pop.append(mutated_ind)
    return mutated_pop


# Put all steps together to create the next generation

def next_generation(currentGen, eliteSize, mutationRate):
    pop_ranked = rank_routes(currentGen)
    selection_results = selection(pop_ranked, eliteSize)
    matingpool = mating_pool(currentGen, selection_results)
    children = breed_population(matingpool, eliteSize)
    next_gen = mutate_population(children, mutationRate)
    return next_gen


# Final step: create the genetic algorithm

def genetic_algorithm(district_list, popSize, eliteSize, mutationRate, generations):
    list_best_route = []
    pop = initial_population(popSize, district_list)
    progress = [1 / rank_routes(pop)[0][1]]
    print("Initial distance: " + str(progress[0]))

    for i in range(1, generations + 1):

        pop = next_generation(pop, eliteSize, mutationRate)
        list_best_route.append(pop[0])
        progress.append(1 / rank_routes(pop)[0][1])
        if i % 5 == 0:
            print('Generation ' + str(i), "Distance: ", progress[i])



    best_route_index = rank_routes(pop)[0][0]
    best_route = pop[best_route_index]
    print(list_best_route)
    print(best_route);

    return ResponseTsp(progress= progress,list_best_route= list_best_route)