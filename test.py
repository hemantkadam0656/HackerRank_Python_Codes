import numpy as np

# Step 1: Create a dataset (rows: observations, columns: features)
data = np.array([
    [2.5, 2.4],
    [0.5, 0.7],
    [2.2, 2.9],
    [1.9, 2.2],
    [3.1, 3.0],
    [2.3, 2.7],
    [2, 1.6],
    [1, 1.1],
    [1.5, 1.6],
    [1.1, 0.9]
])

# Step 2: Center the data (subtract mean from each feature)
mean = np.mean(data, axis=0)
centered_data = data - mean

# Step 3: Compute covariance matrix manually
cov_matrix_manual = np.dot(centered_data.T, centered_data) / (data.shape[0] - 1)
# Step 4: Compute covariance matrix using NumPy
cov_matrix_np = np.cov(data.T)

# Print results
print("Covariance Matrix (Manual Calculation):\n", cov_matrix_manual)
print("Covariance Matrix (NumPy):\n", cov_matrix_np)
