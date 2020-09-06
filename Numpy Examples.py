# Creating a Matrxi without using Numpy
default = [[56.0,0.0,4.4,68.0],[1.2,104.2,52.0,8.0],[1.8,135.0,99.0,0.9]]


# Creating a Matrix using Numpy. Its also called an Array. 
import numpy as np
a = np.array([1, 2, 3])
print(a)               # Output: [1, 2, 3]
print(type(a))         # Output: <class 'numpy.ndarray'>

A = np.array([[1, 2, 3], [3, 4, 5]]) # Array of integer numbers
print(A)

A = np.array([[1, 2, 3], [3, 4, 5]], dtype = complex) # Array of complex numbers
print(A)
# ----------------------------------------------------------------------------------------
A = np.array([[56.0,0.0,4.4,68.0],[1.2,104.2,52.0,8.0],[1.8,135.0,99.0,0.9]])
print(A)

cal = A.sum(axis=0) # .sum() attribute to do row or column wise summation of matrix elements

percentage = 100*A/cal # An example of how broadcasting works with numpy arrays.

a = np.random.randn(10).reshape(5,2) ### numpy random object using the random class and .randn() attribute and .reshape() method

## Matrix Multiplication

C = np.array([[3, 6, 7], [5, -3, 0]])
B = np.array([[1, 1], [2, 1], [3, -3]])
D = C.dot(B)
print(D)
 
# Note: * is used for array multiplication (multiplication of corresponding elements of two arrays) not matrix multiplication.

## Matrix Transpose
E = np.array([[1, 1], [2, 1], [3, -3]])
F = E.transpose()
print(E)
print(F)


print(F.shape) ## Shape attribute of A Matrix - Returns a TUPLE.

#Thank You

