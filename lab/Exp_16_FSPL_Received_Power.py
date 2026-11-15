
import numpy as np
import matplotlib.pyplot as plt

# Experiment 16: Free-Space Path Loss and Received Power

# Given Parameters
frequency = 2.4e9       # Frequency in Hz (2.4 GHz)
transmit_power = 20     # Transmit power in dBm
gain_tx = 2             # Transmitter antenna gain in dBi
gain_rx = 2             # Receiver antenna gain in dBi
c = 3e8                 # Speed of light in m/s

# Distance range (1 to 1000 meters)
distance = np.linspace(1, 1000, 100)

# Calculate Free-Space Path Loss
fspl = 20 * np.log10(
    (4 * np.pi * distance * frequency) / c
)

# Calculate Received Power
received_power = transmit_power + gain_tx + gain_rx - fspl

# Display Simulation Results
print("========================================")
print(" FREE SPACE PATH LOSS AND RECEIVED POWER")
print("========================================")
print("Frequency:", frequency / 1e9, "GHz")
print("Transmit Power:", transmit_power, "dBm")

print("\nDistance(m)    FSPL(dB)    Received Power(dBm)")
print("--------------------------------------------")

for i in [0, 24, 49, 74, 99]:
    print(
        f"{distance[i]:10.2f}"
        f"{fspl[i]:14.2f}"
        f"{received_power[i]:20.2f}"
    )

# Graph 1: Free Space Path Loss
plt.figure(figsize=(9, 5))
plt.plot(distance, fspl, linewidth=2, label="FSPL")
plt.xlabel("Distance (meters)")
plt.ylabel("Path Loss (dB)")
plt.title("Free Space Path Loss vs Distance")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Graph 2: Received Power
plt.figure(figsize=(9, 5))
plt.plot(distance, received_power, color="green",
         linewidth=2, label="Received Power")
plt.xlabel("Distance (meters)")
plt.ylabel("Received Power (dBm)")
plt.title("Received Power vs Distance")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print("\nSimulation Completed Successfully!")
