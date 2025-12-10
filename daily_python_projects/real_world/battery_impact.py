import matplotlib.pyplot as plt

# Define battery parameters
initial_capacity = 100.0  # in %
cycle_life = 2000
initial_impedance = 0.05  # Ohms, typical low impedance for Li-ion cell
current = 2.0  # charging/discharging current in Amperes

# Initialize lists to store results
cycles = []
capacities = []
impedances = []
heat_generated = []

# Define degradation rate
capacity_fade_per_cycle = initial_capacity / cycle_life  # simplistic linear degradation
impedance_increase_per_cycle = 0.00002  # Ohms per cycle (example value)

# Simulate over cycles
capacity = initial_capacity
impedance = initial_impedance

for cycle in range(1, cycle_life + 1):
    # Update capacity
    capacity -= capacity_fade_per_cycle
    capacity = max(capacity, 0)  # capacity can't go negative

    # Update impedance
    impedance += impedance_increase_per_cycle

    # Calculate heat generated during this cycle (P = I^2 * R)
    heat = current ** 2 * impedance  # in Watts (assuming 1 second for simplicity)

    # Store results
    cycles.append(cycle)
    capacities.append(capacity)
    impedances.append(impedance)
    heat_generated.append(heat)

# Plotting results
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(cycles, capacities, label='Capacity (%)', color='green')
plt.ylabel('Capacity (%)')
plt.title('Lithium-ion Cell Degradation over Charge-Discharge Cycles')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(cycles, impedances, label='Impedance (Ohms)', color='red')
plt.ylabel('Impedance (Ohms)')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(cycles, heat_generated, label='Heat Generated (W)', color='orange')
plt.xlabel('Cycle Number')
plt.ylabel('Heat (Watts)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
