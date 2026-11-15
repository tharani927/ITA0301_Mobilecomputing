
import numpy as np
import matplotlib.pyplot as plt

# Experiment 17: Frequency Reuse
# Cluster Size, Capacity and S/I Ratio

# Given Parameters
total_channels = 420
reuse_distance_ratio = []
cluster_sizes = np.array([1, 3, 4, 7, 12, 19])
path_loss_exponent = 4
interfering_cells = 6

# Calculations
capacity = total_channels / cluster_sizes

for N in cluster_sizes:
    Q = np.sqrt(3 * N)
    reuse_distance_ratio.append(Q)

reuse_distance_ratio = np.array(reuse_distance_ratio)

# Calculate Signal to Interference Ratio
S_I = (reuse_distance_ratio ** path_loss_exponent) / interfering_cells

# Convert into dB
S_I_dB = 10 * np.log10(S_I)

# Display Results
print("==========================================")
print("       FREQUENCY REUSE SIMULATION")
print("==========================================")

print("\nCluster Size | Reuse Distance | Capacity | S/I (dB)")
print("---------------------------------------------------")

for i in range(len(cluster_sizes)):
    print(
        f"{cluster_sizes[i]:12d} | "
        f"{reuse_distance_ratio[i]:14.2f} | "
        f"{capacity[i]:8.2f} | "
        f"{S_I_dB[i]:8.2f}"
    )

# Graph 1: Cluster Size vs Capacity
plt.figure(figsize=(9, 5))
plt.plot(cluster_sizes, capacity, marker='o',
         linewidth=2, label="System Capacity per Cell")
plt.xlabel("Cluster Size (N)")
plt.ylabel("Channels per Cell")
plt.title("Cluster Size vs Network Capacity")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Graph 2: Cluster Size vs S/I Ratio
plt.figure(figsize=(9, 5))
plt.plot(cluster_sizes, S_I_dB, marker='s',
         color='red', linewidth=2, label="S/I Ratio")
plt.xlabel("Cluster Size (N)")
plt.ylabel("Signal to Interference Ratio (dB)")
plt.title("Cluster Size vs S/I Ratio")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Graph 3: Frequency Reuse Distance
plt.figure(figsize=(9, 5))
plt.bar(cluster_sizes, reuse_distance_ratio,
        width=1.2, label="D/R Ratio")
plt.xlabel("Cluster Size (N)")
plt.ylabel("Reuse Distance Ratio (D/R)")
plt.title("Cluster Size vs Reuse Distance")
plt.grid(axis='y')
plt.legend()
plt.tight_layout()
plt.show()

print("\nSimulation Completed Successfully!")
