"""Genetic Algorithm for Delivery Route Optimisation.
Depot = A. Deliveries = B..G. Goal: shortest round trip A -> ... -> A.
"""
import random
from itertools import permutations

# ---- Distance matrix (km), symmetric ----
LOCATIONS = ["A", "B", "C", "D", "E", "F", "G"]
DIST = {
    "A": {"A": 0, "B": 4, "C": 8, "D": 6, "E": 7, "F": 9, "G": 5},
    "B": {"A": 4, "B": 0, "C": 5, "D": 7, "E": 3, "F": 8, "G": 6},
    "C": {"A": 8, "B": 5, "C": 0, "D": 4, "E": 6, "F": 3, "G": 7},
    "D": {"A": 6, "B": 7, "C": 4, "D": 0, "E": 5, "F": 6, "G": 8},
    "E": {"A": 7, "B": 3, "C": 6, "D": 5, "E": 0, "F": 4, "G": 6},
    "F": {"A": 9, "B": 8, "C": 3, "D": 6, "E": 4, "F": 0, "G": 5},
    "G": {"A": 5, "B": 6, "C": 7, "D": 8, "E": 6, "F": 5, "G": 0},
}
DEPOT = "A"
DELIVERIES = ["B", "C", "D", "E", "F", "G"]

# ---- GA parameters ----
POPULATION_SIZE = 30
GENERATIONS = 100          # at least 50
MUTATION_RATE = 0.2
ELITE_COUNT = 2            # best routes copied unchanged
TOURNAMENT_SIZE = 3
SEED = 7                   # fixed seed -> reproducible result

random.seed(SEED)


def route_distance(chromosome):
    """Total distance of A -> chromosome -> A (includes return to depot)."""
    path = [DEPOT] + chromosome + [DEPOT]
    return sum(DIST[path[i]][path[i + 1]] for i in range(len(path) - 1))


def create_individual():
    """A chromosome is a random order of B-G (A is added at start/end)."""
    route = DELIVERIES[:]
    random.shuffle(route)
    return route


def create_population():
    return [create_individual() for _ in range(POPULATION_SIZE)]


def tournament_selection(population):
    """Pick random routes, return the shortest one (parent selection)."""
    contestants = random.sample(population, TOURNAMENT_SIZE)
    return min(contestants, key=route_distance)


def ordered_crossover(parent1, parent2):
    """Copy a slice from parent1, fill the rest in parent2's order.
    Child has every location exactly once (valid route)."""
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[start:end + 1] = parent1[start:end + 1]
    remaining = [gene for gene in parent2 if gene not in child]
    for i in range(len(child)):
        if child[i] is None:
            child[i] = remaining.pop(0)
    return child


def swap_mutation(chromosome):
    """Swap two delivery stops (still a valid route)."""
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(len(chromosome)), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome


def run_ga():
    population = create_population()
    best = min(population, key=route_distance)

    for generation in range(1, GENERATIONS + 1):
        population.sort(key=route_distance)
        next_generation = [r[:] for r in population[:ELITE_COUNT]]  # elitism

        while len(next_generation) < POPULATION_SIZE:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child = ordered_crossover(parent1, parent2)
            child = swap_mutation(child)
            next_generation.append(child)

        population = next_generation
        best = min(population, key=route_distance)
        if generation == 1 or generation % 10 == 0:
            print(f"Generation {generation:3d}: best = "
                  f"{' -> '.join([DEPOT] + best + [DEPOT])}  ({route_distance(best)} km)")
    return best


if __name__ == "__main__":
    best_route = run_ga()
    print("\nBest route found:", " -> ".join([DEPOT] + best_route + [DEPOT]))
    print("Total distance  :", route_distance(best_route), "km")

    # Check against brute force (only 6! = 720 routes)
    optimum = min(route_distance(list(p)) for p in permutations(DELIVERIES))
    print("Optimal distance (brute force check):", optimum, "km")
