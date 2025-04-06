import numpy as np
import matplotlib.pyplot as plt

# 1. Generate 1000 random numbers with mean 5 and std deviation 2
normal_data = np.random.normal(5, 2, 1000)

# 2. Create x values from 0 to 10 (for plotting h(x) = x^3)
x = np.linspace(0, 10, 100)  # 100 points between 0 and 10
y = x**3  # h(x) = x^3

# 3. Create the plot
plt.figure(figsize=(10, 6))

# Plot the histogram
plt.hist(normal_data, bins=30, alpha=0.6, label='Normal Distribution', color='skyblue', edgecolor='black')

# Plot the function h(x) = x^3
plt.plot(x, y, label='h(x) = x³', color='red', linewidth=2)

# Add labels and title
plt.title('Histogram + h(x) = x³')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add legend
plt.legend()

# Show the plot
plt.show()
