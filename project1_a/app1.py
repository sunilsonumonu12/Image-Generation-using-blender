import random
import os

# Define the list of names to check against
possible_names = ["sunil", "raj", "sonu", "john", "doe"]  # Add more names as needed

# Genetic Algorithm parameters
POPULATION_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.1

def fitness_function(individual):
    """Evaluate the fitness of an individual."""
    x1, y1, x2, y2 = individual

    # Ensure coordinates are in the range [0, 1]
    if not (0 <= x1 <= 1 and 0 <= y1 <= 1 and 0 <= x2 <= 1 and 0 <= y2 <= 1):
        return 0  # Invalid coordinates, return low fitness
    
    # Penalize if the difference between y1 and y2 is not 0.2
    if abs(y1 - y2) != 0.2:
        return 0  # Invalid fitness if difference condition is not met
    
    # Fitness based on proximity to the center (0.5, 0.5)
    name_distance = ((x1 - 0.5) ** 2 + (y1 - 0.5) ** 2) ** 0.5
    non_name_distance = ((x2 - 0.5) ** 2 + (y2 - 0.5) ** 2) ** 0.5
    
    # The fitness score combines the distances, lower distance gives higher fitness
    return 1 / (1 + name_distance + non_name_distance)

def mutate(individual):
    """Mutate an individual by randomly changing its coordinates."""
    x1, y1, x2, y2 = individual
    if random.random() < MUTATION_RATE:
        x1 += random.uniform(-0.1, 0.1)
        y1 += random.uniform(-0.1, 0.1)
        x2 += random.uniform(-0.1, 0.1)
        y2 += random.uniform(-0.1, 0.1)
    
    # Ensure coordinates stay within bounds [0, 1]
    x1, x2 = max(0, min(1, x1)), max(0, min(1, x2))
    
    # Maintain the difference of 0.2 between y1 and y2
    if y1 + 0.2 <= 1:
        y2 = y1 + 0.2
    else:
        y2 = y1 - 0.2
    
    y1 = max(0, min(1, y1))
    y2 = max(0, min(1, y2))
    
    return x1, y1, x2, y2

def crossover(parent1, parent2):
    """Cross over two parents to produce an offspring."""
    x1 = (parent1[0] + parent2[0]) / 2
    y1 = (parent1[1] + parent2[1]) / 2
    x2 = (parent1[2] + parent2[2]) / 2
    y2 = (parent1[3] + parent2[3]) / 2
    
    # Maintain the difference of 0.2 between y1 and y2
    if y1 + 0.2 <= 1:
        y2 = y1 + 0.2
    else:
        y2 = y1 - 0.2
    
    return x1, y1, x2, y2

def select(population, fitnesses):
    """Select an individual from the population using weighted probability."""
    total_fitness = sum(fitnesses)
    
    # Check if total fitness is zero to avoid division by zero
    if total_fitness == 0:
        return random.choice(population)  # Choose a random individual if no valid fitnesses
    
    selection_probs = [f / total_fitness for f in fitnesses]
    return population[random.choices(range(len(population)), weights=selection_probs)[0]]

def read_input(input_path):
    """Read the input text and classify names and non-names."""
    if not os.path.exists(input_path):
        return "", []

    with open(input_path, 'r') as file:
        text = file.read()
    x_range = (0, 1) 
    
    # Calculate size of the input text
    size = len(text.split())
    if size >= 6:
        decrease_percentage = (size - 5) * 10
        decrease_value = 1 * (decrease_percentage / 100)
        x_range = (0, 1 - decrease_value)

      # 60% for size 6, 70% for size 7, etc.
    
    # Check if the size exceeds 5 and adjust x range accordingly
  # Decrease the range of x by 50%
    
    # Classify names and non-names
    classified_names = []
    classified_non_names = []
    
    for word in text.split():
        if word.lower() in possible_names:
            classified_names.append(word)
        else:
            classified_non_names.append(word)

    return text, classified_names, classified_non_names, x_range

def genetic_algorithm(x_range):
    """Run the genetic algorithm to find optimal coordinates."""
    # Initialize population randomly
    population = [(random.uniform(*x_range), random.uniform(0, 1), 
                   random.uniform(*x_range), random.uniform(0, 1))
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

def save_outputs(name_output_path, non_name_output_path, name_coordinates_output_path, non_name_coordinates_output_path, names, non_names, coordinates):
    """Save the classified names, non-names, and coordinates to output files."""
    with open(name_output_path, 'w') as file:
        file.write("\n".join(names))

    with open(non_name_output_path, 'w') as file:
        file.write("\n".join(non_names))

    with open(name_coordinates_output_path, 'w') as file:
        file.write(f"{coordinates[0]}, {coordinates[1]}\n")  # (x1, y1)

    with open(non_name_coordinates_output_path, 'w') as file:
        file.write(f"{coordinates[2]}, {coordinates[3]}\n")  # (x2, y2)

# Define output paths
name_output_path = r"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\project1_a\name_output.txt"
non_name_output_path = r"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\project1_a\non_name_output.txt"
name_coordinates_output_path = r"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\project1_a\name_coordinates.txt"
non_name_coordinates_output_path = r"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\project1_a\non_name_coordinates.txt"

# Read from input text
input_path = r"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\project1_a\input_text.txt"
text, names, non_names, x_range = read_input(input_path)

# Run the genetic algorithm
optimal_coordinates = genetic_algorithm(x_range)
print(f"Optimal Coordinates for Name and Non-Name: {optimal_coordinates}")

# Save outputs
save_outputs(name_output_path, non_name_output_path, name_coordinates_output_path, non_name_coordinates_output_path, names, non_names, optimal_coordinates)
