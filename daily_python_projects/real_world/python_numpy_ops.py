import numpy as np

# 1. Array creation
arr1 = np.array([1, 2, 3, 4, 5])  # 1D array
arr2 = np.array([[1, 2], [3, 4]])  # 2D array
arr3 = np.zeros((3, 3))  # Array of zeros
arr4 = np.ones((2, 3))  # Array of ones
arr5 = np.arange(0, 10, 2)  # Array with a range
arr6 = np.linspace(0, 1, 5)  # Array with linearly spaced values

print("Array 1 (1D):", arr1)
print("Array 2 (2D):", arr2)
print("Zeros Array:", arr3)
print("Ones Array:", arr4)
print("Range Array:", arr5)
print("Linspace Array:", arr6)

# 2. Array attributes
print("\nShape of Array 2:", arr2.shape)
print("Data type of Array 1:", arr1.dtype)
print("Number of dimensions of Array 2:", arr2.ndim)

# 3. Array Reshaping
reshaped_arr = arr1.reshape((5, 1))  # Reshaping 1D array to 2D
print("\nReshaped Array:", reshaped_arr)

# 4. Array Indexing and Slicing
print("\nFirst two elements of Array 1:", arr1[:2])
print("Last element of Array 2:", arr2[-1, -1])

# 5. Mathematical Operations
sum_arr = arr1 + 10  # Adding scalar to array
prod_arr = arr1 * 2  # Multiplying scalar to array
elementwise_prod = arr1 * arr1  # Element-wise multiplication
dot_product = np.dot(arr1, np.array([1, 2, 3, 4, 5]))  # Dot product
mean_arr = np.mean(arr1)  # Mean of elements
sum_arr_all = np.sum(arr2)  # Sum of all elements in 2D array

print("\nArray 1 + 10:", sum_arr)
print("Array 1 * 2:", prod_arr)
print("Element-wise multiplication of Array 1 with itself:", elementwise_prod)
print("Dot product of Array 1 with another array:", dot_product)
print("Mean of Array 1:", mean_arr)
print("Sum of all elements in Array 2:", sum_arr_all)

# 6. Broadcasting Example
# broadcasted_arr = arr1 + arr3[:, 0]  # Broadcasting a 2D array operation
# print("\nBroadcasting result:", broadcasted_arr)

# 7. Statistical Functions
print("\nMax of Array 1:", np.max(arr1))
print("Min of Array 1:", np.min(arr1))
print("Standard deviation of Array 1:", np.std(arr1))
print("Variance of Array 1:", np.var(arr1))

# 8. Linear Algebra
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Matrix multiplication (dot product)
matrix_mult = np.dot(matrix_a, matrix_b)
print("\nMatrix multiplication (A * B):\n", matrix_mult)

# Determinant of a matrix
determinant = np.linalg.det(matrix_a)
print("Determinant of Matrix A:", determinant)

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix_a)
print("\nEigenvalues of Matrix A:", eigenvalues)
print("Eigenvectors of Matrix A:\n", eigenvectors)

# 9. Random Module
random_arr = np.random.random((2, 3))  # Random values between 0 and 1
random_int_arr = np.random.randint(1, 10, size=(2, 3))  # Random integers between 1 and 10
randn_arr = np.random.randn(2, 3)  # Random values from normal distribution

print("\nRandom array:", random_arr)
print("Random integer array:", random_int_arr)
print("Random normal array:", randn_arr)

# 10. Sorting
sorted_arr = np.sort(arr1)  # Sorting the array
print("\nSorted Array 1:", sorted_arr)

# 11. Stacking and Splitting
stacked_arr = np.vstack((arr1, arr5))  # Stack arrays vertically
h_stacked_arr = np.hstack((arr1, arr5))  # Stack arrays horizontally
split_arr = np.split(stacked_arr, 2)  # Split array into 2

print("\nVertically stacked array:\n", stacked_arr)
print("Horizontally stacked array:\n", h_stacked_arr)
print("Split array:", split_arr)

# 12. Copy vs View
arr_copy = arr1.copy()  # Creating a copy
arr_view = arr1.view()   # Creating a view

arr1[0] = 10  # Modify original
print("\nOriginal array after modification:", arr1)
print("Copy of original (no change):", arr_copy)
print("View of original (change reflected):", arr_view)

