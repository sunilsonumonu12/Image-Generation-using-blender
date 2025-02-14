import random

def get_text_coordinates(size_category):
    """Gets the box coordinates based on size category."""
    box_width = 1  # Original width
    box_height = 0.5  # Original height

    if size_category == "medium":
        box_width *= 0.5
        box_height *= 0.5
    elif size_category == "large":
        box_width *= 0.25  # Further decrease by 50% from medium

    # Calculate centered position for the adjusted box size
    center_x = 0.5  # Original center x
    center_y = 0.35  # Original center y

    # Adjust coordinates based on the new size
    bottom_left = (center_x - box_width / 2, center_y - box_height / 2)
    top_right = (center_x + box_width / 2, center_y + box_height / 2)

    return bottom_left, top_right

def generate_individual(size_category):
    """Generates a random set of coordinates based on size category."""
    if size_category == "small":
        return get_text_coordinates("small")
    elif size_category == "medium":
        return get_text_coordinates("medium")
    elif size_category == "large":
        return get_text_coordinates("large")
    return None

def fitness(coordinates):
    """Calculates fitness based on how well the coordinates accommodate the text."""
    box_width = coordinates[1][0] - coordinates[0][0]
    box_height = coordinates[1][1] - coordinates[0][1]
    return box_width * box_height  # Maximize the area of the box

def selection(population):
    """Selects two individuals based on their fitness (roulette selection)."""
    total_fitness = sum(fitness(ind) for ind in population)
    selection_probs = [fitness(ind) / total_fitness for ind in population]
    parent1 = random.choices(population, weights=selection_probs, k=1)[0]
    parent2 = random.choices(population, weights=selection_probs, k=1)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    """Performs crossover between two parents to produce offspring."""
    child = []
    for i in range(2):  # Assuming two coordinates (bottom left and top right)
        child.append(random.choice([parent1[i], parent2[i]]))
    return child

def mutate(individual, mutation_rate=0.1):
    """Applies mutation to an individual."""
    if random.random() < mutation_rate:
        individual[0] = (random.uniform(0, 1), random.uniform(0, 2))  # Mutate bottom left
    if random.random() < mutation_rate:
        individual[1] = (random.uniform(0, 1), random.uniform(0, 2))  # Mutate top right
    return individual

def genetic_algorithm(size_category, population_size=100, generations=50):
    # Initialize population
    population = [generate_individual(size_category) for _ in range(population_size)]
    
    for generation in range(generations):
        new_population = []
        for _ in range(population_size // 2):  # Pairing parents
            parent1, parent2 = selection(population)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            new_population.extend([mutate(child1), mutate(child2)])
        population = new_population  # Replace old population with new

    # Get the best individual
    best_individual = max(population, key=fitness)
    
    # Return only the bottom left coordinate
    return best_individual[0]  # Return only the bottom left coordinate

# Example usage
size_category = "large"  # This can be set dynamically based on text length
best_coordinate = genetic_algorithm(size_category)

# Define the file path correctly
file_path = r"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\python_july19\input2.txt"

# Save the best coordinate to input2.txt
with open(file_path, 'w') as file:
    file.write(f"{best_coordinate[0]}, {best_coordinate[1]}\n")

print(f"Best Bottom Left Coordinate for Text Object: {best_coordinate}")
