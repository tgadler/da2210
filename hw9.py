import matplotlib.pyplot as plt
import random

# Simulation parameters
X = 10000000
number_of_simulations = 100000
all_runs_avgs = []

# Function for coin toss
def coin_toss():
    return random.random() < 0.5

# Running the simulation five times
for run in range(5):
    results = []
    avgs = []
    
    for i in range(number_of_simulations):
        payout = 1
        
        while(coin_toss() and payout < X):
            payout *= 2

        results.append(payout)
        avgs.append(sum(results) / len(results))

    all_runs_avgs.append(avgs)

    # Plot each run
    plt.plot(avgs, label=f'Run {run + 1}')

# Calculate and plot the average of all runs
average_of_all_runs = [sum(avgs) / len(avgs) for avgs in zip(*all_runs_avgs)]
plt.plot(average_of_all_runs, label='Average of All Runs', linewidth=2, linestyle='--', color='black')

# Set y-axis limit
plt.ylim(0, 20)

# Plot settings
plt.xlabel('Number of Simulations')
plt.ylabel('Average Payout')
plt.title('Average Payout over Simulations for 5 Runs')
plt.legend()
plt.grid(True)
plt.show()
