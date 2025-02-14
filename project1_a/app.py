import random

# Genetic Algorithm parameters
POPULATION_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.1

def fitness_function(individual):
    """Evaluate the fitness of an individual.
    The individual is a tuple (x1, y1, x2, y2).
    """
    x1, y1, x2, y2 = individual
    
    # Ensure coordinates are in the range [0, 1]
    if not (0 <= x1 <= 1 and 0 <= y1 <= 1 and 0 <= x2 <= 1 and 0 <= y2 <= 1):
        return 0  # Invalid coordinates, return low fitness
    
    # Fitness based on how well-separated the coordinates are
    # Aim for "name" coordinates (x1, y1) to be close to the center (0.5, 0.5)
    # and "non-name" coordinates (x2, y2) to be further away from "name"
    name_distance = ((x1 - 0.5) ** 2 + (y1 - 0.5) ** 2) ** 0.5
    non_name_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    # Favor smaller name_distance and larger non_name_distance
    return 1 / (1 + name_distance) + non_name_distance

def mutate(individual):
    """Mutate an individual by randomly changing one of its coordinates."""
    x1, y1, x2, y2 = individual
    if random.random() < MUTATION_RATE:
        x1 += random.uniform(-0.1, 0.1)
        y1 += random.uniform(-0.1, 0.1)
        x2 += random.uniform(-0.1, 0.1)
        y2 += random.uniform(-0.1, 0.1)
    # Ensure coordinates stay within bounds [0, 1]
    return max(0, min(1, x1)), max(0, min(1, y1)), max(0, min(1, x2)), max(0, min(1, y2))

def crossover(parent1, parent2):
    """Cross over two parents to produce an offspring."""
    x1 = (parent1[0] + parent2[0]) / 2
    y1 = (parent1[1] + parent2[1]) / 2
    x2 = (parent1[2] + parent2[2]) / 2
    y2 = (parent1[3] + parent2[3]) / 2
    return x1, y1, x2, y2

def select(population, fitnesses):
    """Select an individual from the population using weighted probability."""
    total_fitness = sum(fitnesses)
    selection_probs = [f / total_fitness for f in fitnesses]
    return population[random.choices(range(len(population)), weights=selection_probs)[0]]

def genetic_algorithm():
    """Run the genetic algorithm to find optimal coordinates."""
    # Initialize population randomly
    population = [(random.random(), random.random(), random.random(), random.random())
                  for _ in range(POPULATION_SIZE)]
    
    for generation in range(GENERATIONS):
        # Evaluate fitness for each individual
        fitnesses = [fitness_function(individual) for individual in population]
        
        # Create a new population
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            # Select two parents
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            
            # Crossover
            offspring1 = crossover(parent1, parent2)
            offspring2 = crossover(parent2, parent1)
            
            # Mutate offspring
            offspring1 = mutate(offspring1)
            offspring2 = mutate(offspring2)
            
            # Add offspring to new population
            new_population.extend([offspring1, offspring2])
        
        # Update population
        population = new_population
        
        # Print best fitness in the current generation
        best_fitness = max(fitnesses)
        print(f"Generation {generation + 1}, Best Fitness: {best_fitness}")
    
    # Get the best individual
    best_individual = max(population, key=fitness_function)
    return best_individual

# Prepare output paths
name_output_path = r"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\project1_a\name_output.txt"
non_name_output_path = r"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\project1_a\non_name_output.txt"
name_coordinates_output_path = r"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\project1_a\name_coordinates.txt"
non_name_coordinates_output_path = r"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\project1_a\non_name_coordinates.txt"

# Example name and non-name text
name_text = "John Doe"
non_name_text = "Some other text"

# Run the genetic algorithm to find optimal coordinates
optimal_coordinates = genetic_algorithm()
x1, y1, x2, y2 = optimal_coordinates

# Save the name text to the name output file
with open(name_output_path, 'w') as name_file:
    name_file.write(f"{name_text}\n")

# Save the coordinates for the name text
with open(name_coordinates_output_path, 'w') as name_coord_file:
    name_coord_file.write(f"{x1}, {y1}\n")

# Save the non-name text to the non-name output file
with open(non_name_output_path, 'w') as non_name_file:
    non_name_file.write(f"{non_name_text}\n")

# Save the coordinates for the non-name text
with open(non_name_coordinates_output_path, 'w') as non_name_coord_file:
    non_name_coord_file.write(f"{x2}, {y2}\n")

print(f"Optimal Coordinates for Name: ({x1}, {y1})")
print(f"Optimal Coordinates for Non-Name: ({x2}, {y2})")
