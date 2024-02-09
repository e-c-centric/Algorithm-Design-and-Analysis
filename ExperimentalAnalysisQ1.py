import matplotlib.pyplot as plt

input_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
counts = [11966, 24303, 39992, 53010, 67272, 78692, 91274, 113063, 129799, 140538]

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, counts, marker='o', linestyle='-', color='b', label='Count vs. Input Size')

plt.xlabel('Input Size')
plt.ylabel('Count')
plt.title('Count vs. Input Size')
plt.legend()

plt.grid(True)
plt.show()