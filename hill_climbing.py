import random

# Define the fitness function to optimize (minimize)
def fitness_function(x):
    return (x - 5) ** 2

# Define the hill climbing function
def hill_climbing(starting_point, step_size, max_iterations):
    # Initialize the current point
    current_point = starting_point
    # Iterate until the maximum number of iterations is reached or no better neighbor can be found
    for i in range(max_iterations):
        # Generate a neighbor by adding or subtracting the step size from the current point
        neighbor = current_point + random.uniform(-step_size, step_size)
        # Evaluate the fitness of the current point and the neighbor
        current_fitness = fitness_function(current_point)
        neighbor_fitness = fitness_function(neighbor)
        # If the neighbor has a lower fitness, move to the neighbor
        if neighbor_fitness < current_fitness:
            current_point = neighbor
    # Return the final point
    return current_point

# Test the hill climbing function
starting_point = 0
step_size = 0.1
max_iterations = 1000
best_point = hill_climbing(starting_point, step_size, max_iterations)
print("Best point found:", best_point)
print("Fitness of best point:", fitness_function(best_point))