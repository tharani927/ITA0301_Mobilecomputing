
import numpy as np
import matplotlib.pyplot as plt

# Experiment 21: OFDMA Downlink Scheduler

# Simulation Parameters
num_users = 5
num_resource_blocks = 100

# User channel quality (Mbps per resource block)
channel_quality = np.array([8, 6, 4, 3, 2])

# Resource allocation
# 1. Round Robin Scheduler
rr_allocation = np.ones(num_users) * (
    num_resource_blocks / num_users
)

# 2. Proportional Fair Scheduler
pf_weights = channel_quality / np.mean(channel_quality)
pf_allocation = num_resource_blocks * (
    pf_weights / np.sum(pf_weights)
)

# 3. Maximum Throughput Scheduler
mt_allocation = np.zeros(num_users)
best_user = np.argmax(channel_quality)
mt_allocation[best_user] = num_resource_blocks

# Calculate User Throughput
rr_throughput = rr_allocation * channel_quality
pf_throughput = pf_allocation * channel_quality
mt_throughput = mt_allocation * channel_quality

# Jain's Fairness Index
def fairness_index(throughput):
    return (np.sum(throughput) ** 2) / (
        num_users * np.sum(throughput ** 2)
    )

# Calculate Fairness
rr_fairness = fairness_index(rr_throughput)
pf_fairness = fairness_index(pf_throughput)
mt_fairness = fairness_index(mt_throughput)

# Display Results
print("========================================")
print("      OFDMA DOWNLINK SCHEDULER")
print("========================================")

print("\nUser Channel Quality:")
print(channel_quality)

print("\nRound Robin Throughput:")
print(rr_throughput)

print("\nProportional Fair Throughput:")
print(pf_throughput)

print("\nMaximum Throughput:")
print(mt_throughput)

print("\nFairness Index:")
print("Round Robin:", round(rr_fairness, 4))
print("Proportional Fair:", round(pf_fairness, 4))
print("Maximum Throughput:", round(mt_fairness, 4))

# Graph 1: User Throughput Comparison
users = np.arange(1, num_users + 1)
width = 0.25

plt.figure(figsize=(10, 5))

plt.bar(users - width, rr_throughput,
        width, label="Round Robin")

plt.bar(users, pf_throughput,
        width, label="Proportional Fair")

plt.bar(users + width, mt_throughput,
        width, label="Maximum Throughput")

plt.xlabel("User Number")
plt.ylabel("Throughput (Mbps)")
plt.title("OFDMA Scheduler Throughput Comparison")
plt.xticks(users)
plt.grid(axis="y")
plt.legend()
plt.tight_layout()
plt.show()

# Graph 2: Fairness Comparison
scheduler_names = [
    "Round Robin",
    "Proportional Fair",
    "Maximum Throughput"
]

fairness_values = [
    rr_fairness,
    pf_fairness,
    mt_fairness
]

plt.figure(figsize=(9, 5))
plt.bar(scheduler_names, fairness_values)

plt.xlabel("Scheduling Algorithm")
plt.ylabel("Jain's Fairness Index")
plt.title("Fairness Comparison of OFDMA Schedulers")
plt.ylim(0, 1.1)
plt.grid(axis="y")
plt.tight_layout()
plt.show()

print("\nSimulation Completed Successfully!")
