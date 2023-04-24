import math
import random

# Define the objective function to minimize
def objective_function(x):
    return x**2 + 3*x + 5

# Define the acceptance probability function
def acceptance_probability(old_cost, new_cost, temperature):
    if new_cost < old_cost:
        return 1.0
    else:
        return math.exp((old_cost - new_cost) / temperature)

# Define the simulated annealing function
def simulated_annealing(initial_state, temperature, cooling_rate):
    current_state = initial_state
    current_cost = objective_function(current_state)
    best_state = current_state
    best_cost = current_cost
    while temperature > 1:
        # Generate a new state

        #random.uniform generates with argument -1,1 generates a random value between -1 and 1
        new_state = current_state + random.uniform(-1, 1)
        new_cost = objective_function(new_state)
        # Decide whether to move to the new state
        if acceptance_probability(current_cost, new_cost, temperature) > random.uniform(0, 1):
            current_state = new_state
            current_cost = new_cost
        # Keep track of the best state seen so far
        if current_cost < best_cost:
            best_state = current_state
            best_cost = current_cost
        # Cool the temperature
        temperature *= cooling_rate
        
    return best_state, best_cost

# Test the simulated annealing function
initial_state = 0.0
temperature = 100.0
cooling_rate = 0.99
best_state, best_cost = simulated_annealing(initial_state, temperature, cooling_rate)
print("Best state found:", best_state)
print("Best cost found:", best_cost)