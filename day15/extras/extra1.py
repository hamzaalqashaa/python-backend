import numpy as np

# Generate 10x10 random integers between 1 and 100
array = np.random.randint(1, 101, (10, 10))
print("Original Array:\n", array)

# Mean, Median, Standard Deviation
print("\nMean:", np.mean(array))
print("Median:", np.median(array))
print("Standard Deviation:", np.std(array))

# Extract main diagonal
print("\nMain Diagonal:", np.diag(array))

# Find values greater than 80
print("\nValues greater than 80:", array[array > 80])

# Replace values less than 30 with 0
array[array < 30] = 0
print("\nArray after replacing values less than 30:\n", array)
