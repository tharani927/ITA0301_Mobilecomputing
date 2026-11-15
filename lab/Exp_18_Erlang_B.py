
import matplotlib.pyplot as plt

# Experiment 18: Call Blocking Probability
# Using Erlang B Formula

# Erlang B Calculation
def erlang_b(A, C):
    B = 1.0
    for i in range(1, C + 1):
        B = (A * B) / (i + A * B)
    return B

# Given Parameters
channels = 20
traffic_values = [5, 10, 15, 20, 25, 30, 35, 40]

blocking_probabilities = []

# Calculate Blocking Probability
print("======================================")
print("   CALL BLOCKING PROBABILITY")
print("       USING ERLANG B FORMULA")
print("======================================")

print("\nTraffic (Erlangs) | Blocking Probability (%)")
print("---------------------------------------------")

for traffic in traffic_values:
    blocking = erlang_b(traffic, channels)
    blocking_percent = blocking * 100
    blocking_probabilities.append(blocking_percent)

    print(f"{traffic:17} | {blocking_percent:.4f}")

# Graph 1: Traffic vs Blocking Probability
plt.figure(figsize=(9, 5))
plt.plot(traffic_values, blocking_probabilities,
         marker='o', linewidth=2)

plt.xlabel("Traffic Load (Erlangs)")
plt.ylabel("Blocking Probability (%)")
plt.title("Traffic Load vs Call Blocking Probability")
plt.grid(True)
plt.tight_layout()
plt.show()

# Graph 2: Blocking Probability for Different Channels
channel_values = [5, 10, 15, 20, 25, 30]

plt.figure(figsize=(9, 5))

for C in channel_values:
    probabilities = [
        erlang_b(A, C) * 100 for A in traffic_values
    ]
    plt.plot(traffic_values, probabilities,
             marker='o', label=f"{C} Channels")

plt.xlabel("Traffic Load (Erlangs)")
plt.ylabel("Blocking Probability (%)")
plt.title("Blocking Probability for Different Channel Counts")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print("\nSimulation Completed Successfully!")
