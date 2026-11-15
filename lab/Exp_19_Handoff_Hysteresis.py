
import numpy as np
import matplotlib.pyplot as plt

# Experiment 19: Handoff Simulation with Hysteresis

# Simulation Parameters
time = np.arange(0, 101, 1)

# Signal strength of Base Station 1
signal_bs1 = -50 - 0.5 * time

# Signal strength of Base Station 2
signal_bs2 = -100 + 0.5 * time

# Hysteresis margin in dB
hysteresis = 5

# Initialize handoff variables
serving_bs = []
current_bs = 1
handoff_points = []

# Handoff Decision
for i in range(len(time)):

    if current_bs == 1:
        if signal_bs2[i] > signal_bs1[i] + hysteresis:
            current_bs = 2
            handoff_points.append(time[i])

    else:
        if signal_bs1[i] > signal_bs2[i] + hysteresis:
            current_bs = 1
            handoff_points.append(time[i])

    serving_bs.append(current_bs)

# Display Results
print("======================================")
print("   HANDOFF SIMULATION WITH HYSTERESIS")
print("======================================")

print("Hysteresis Margin:", hysteresis, "dB")
print("Total Handoffs:", len(handoff_points))
print("Handoff Time Points:", handoff_points)

print("\nTime | Serving Base Station")
print("--------------------------")

for i in range(0, len(time), 10):
    print(f"{time[i]:4} | Base Station {serving_bs[i]}")

# Graph 1: Signal Strength
plt.figure(figsize=(10, 5))

plt.plot(time, signal_bs1, label="Base Station 1")
plt.plot(time, signal_bs2, label="Base Station 2")

plt.xlabel("Time")
plt.ylabel("Signal Strength (dBm)")
plt.title("Signal Strength of Two Base Stations")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Graph 2: Serving Base Station
plt.figure(figsize=(10, 5))

plt.step(time, serving_bs, where="post",
         label="Serving Base Station")

for point in handoff_points:
    plt.axvline(point, linestyle="--", label="Handoff")

plt.xlabel("Time")
plt.ylabel("Serving Base Station")
plt.yticks([1, 2], ["Base Station 1", "Base Station 2"])
plt.title("Handoff Decision with Hysteresis")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print("\nSimulation Completed Successfully!")
