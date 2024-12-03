# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.integrate import odeint

# Step 1: Data Generation
# Generate synthetic initial data
num_regions = 5
regions = [f"Region {i}" for i in range(1, num_regions + 1)]
initial_population = np.random.randint(5000, 100000, size=num_regions)
birth_rate = np.random.uniform(0.01, 0.05, size=num_regions)  # 1% to 5%
death_rate = np.random.uniform(0.005, 0.03, size=num_regions)  # 0.5% to 3%
migration_rate = np.random.uniform(-0.02, 0.02, size=num_regions)  # -2% to +2%

# Create a DataFrame for population data
population_data = pd.DataFrame({
    "Region": regions,
    "Initial Population": initial_population,
    "Birth Rate": birth_rate,
    "Death Rate": death_rate,
    "Migration Rate": migration_rate
})

# Print the generated data
print("Generated Population Data:\n")
print(population_data)

# Step 2: Exploratory Data Analysis (EDA)
# Visualize initial population by region
plt.figure(figsize=(8, 6))
sns.barplot(x="Region", y="Initial Population", data=population_data)
plt.title("Initial Population by Region")
plt.xlabel("Region")
plt.ylabel("Population")
plt.show()

# Correlation heatmap of rates
rates_data = population_data[["Birth Rate", "Death Rate", "Migration Rate"]]
plt.figure(figsize=(6, 4))
sns.heatmap(rates_data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Rates")
plt.show()

# Step 3: Modeling
# Define a logistic growth model
def logistic_growth(P, t, r, K):
    """Logistic growth model."""
    return r * P * (1 - P / K)

# Step 4: Simulation
# Simulate population growth for one region (Region 1)
region_index = 0
P0 = population_data["Initial Population"][region_index]  # Initial population
r = population_data["Birth Rate"][region_index] - population_data["Death Rate"][region_index]  # Net growth rate
K = 100000  # Carrying capacity
time = np.linspace(0, 50, 100)  # 50 years

# Solve the logistic growth equation
population = odeint(logistic_growth, P0, time, args=(r, K))

# Plot the simulation results
plt.figure(figsize=(8, 6))
plt.plot(time, population, label=population_data["Region"][region_index], color="blue")
plt.title("Population Dynamics (Logistic Growth)")
plt.xlabel("Time (Years)")
plt.ylabel("Population")
plt.legend()
plt.grid()
plt.show()

# Step 5: Multi-Region Simulation
# Simulate and plot growth for all regions
plt.figure(figsize=(10, 6))
for i in range(num_regions):
    P0 = population_data["Initial Population"][i]
    r = population_data["Birth Rate"][i] - population_data["Death Rate"][i]
    population = odeint(logistic_growth, P0, time, args=(r, K))
    plt.plot(time, population, label=population_data["Region"][i])

plt.title("Population Dynamics for All Regions")
plt.xlabel("Time (Years)")
plt.ylabel("Population")
plt.legend()
plt.grid()
plt.show()

# Step 6: Evaluation and Analysis
# Compare final population sizes
final_population = []
for i in range(num_regions):
    P0 = population_data["Initial Population"][i]
    r = population_data["Birth Rate"][i] - population_data["Death Rate"][i]
    population = odeint(logistic_growth, P0, time, args=(r, K))
    final_population.append(population[-1][0])

population_data["Final Population"] = final_population
print("\nPopulation Data with Final Population:\n")
print(population_data)

# Visualize initial vs final population
plt.figure(figsize=(8, 6))
bar_width = 0.35
index = np.arange(num_regions)

plt.bar(index, population_data["Initial Population"], bar_width, label="Initial Population")
plt.bar(index + bar_width, population_data["Final Population"], bar_width, label="Final Population")

plt.xlabel("Region")
plt.ylabel("Population")
plt.title("Initial vs Final Population by Region")
plt.xticks(index + bar_width / 2, population_data["Region"])
plt.legend()
plt.show()
