
import numpy as np
import matplotlib.pyplot as plt

# Experiment 20: CDMA Spreading and Despreading

# Original binary data
data = np.array([1, 0, 1, 1, 0])

# Convert binary data into bipolar format
bipolar_data = 2 * data - 1

# Spreading code
spreading_code = np.array([1, -1, 1, -1])

# Spreading Process
spread_signal = []

for bit in bipolar_data:
    spread_signal.extend(bit * spreading_code)

spread_signal = np.array(spread_signal)

# Despreading Process
despread_data = []

for i in range(0, len(spread_signal), len(spreading_code)):
    chips = spread_signal[i:i + len(spreading_code)]

    result = np.sum(chips * spreading_code)

    if result > 0:
        despread_data.append(1)
    else:
        despread_data.append(0)

despread_data = np.array(despread_data)

# Display Results
print("======================================")
print("       CDMA SPREADING SIMULATION")
print("======================================")

print("\nOriginal Data:")
print(data)

print("\nSpreading Code:")
print(spreading_code)

print("\nSpread Signal:")
print(spread_signal)

print("\nDespread Data:")
print(despread_data)

print("\nData Recovery Successful:",
      np.array_equal(data, despread_data))

# Graph 1: Original Data
plt.figure(figsize=(10, 4))
plt.step(range(len(data)), data, where="mid",
         linewidth=2)
plt.title("Original Binary Data")
plt.xlabel("Bit Index")
plt.ylabel("Bit Value")
plt.yticks([0, 1])
plt.grid(True)
plt.tight_layout()
plt.show()

# Graph 2: Spread Signal
plt.figure(figsize=(12, 4))
plt.step(range(len(spread_signal)), spread_signal,
         where="mid", color="red", linewidth=2)
plt.title("CDMA Spread Signal")
plt.xlabel("Chip Index")
plt.ylabel("Chip Value")
plt.yticks([-1, 1])
plt.grid(True)
plt.tight_layout()
plt.show()

# Graph 3: Despread Data
plt.figure(figsize=(10, 4))
plt.step(range(len(despread_data)), despread_data,
         where="mid", color="green", linewidth=2)
plt.title("Recovered Data After Despreading")
plt.xlabel("Bit Index")
plt.ylabel("Bit Value")
plt.yticks([0, 1])
plt.grid(True)
plt.tight_layout()
plt.show()

print("\nSimulation Completed Successfully!")

