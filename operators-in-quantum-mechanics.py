import numpy as np

def is_hermitian(matrix):
    if np.allclose(matrix, matrix.conj().T):
        print("\nHermitian: YES")
        print("Reason: A = A† (conjugate transpose).")
    else:
        print("\nHermitian: NO")
        print("Reason: A != A†.")

def is_unitary(matrix):
    I = np.eye(matrix.shape[0])
    U_dagger = matrix.conj().T
    if np.allclose(U_dagger @ matrix, I):
        print("\nUnitary: YES")
        print("Reason: U†U = I and UU† = I.")
    else:
        print("\nUnitary: NO")
        print("Reason: U†U != I or UU† != I.")

def is_projection(matrix):
    if np.allclose(matrix @ matrix, matrix) and np.allclose(matrix, matrix.conj().T):
        print("\nProjection: YES")
        print("Reason: P² = P and P = P†.")
    else:
        print("\nProjection: NO")
        print("Reason: P² != P or P != P†.")

while True:
    n = int(input("Enter the order of the matrix (n): "))
    print("Enter the matrix elements row-wise:")
    A = np.zeros((n, n), dtype=complex)
    print("For complex numbers, enter in the form a+bj (e.g., 1+2j).")
    for i in range(n):
        for j in range(n):
            A[i][j] = complex(input(f"A[{i+1}][{j+1}]: "))
    print("\nMatrix A:")
    print(A)
    is_hermitian(A)
    is_unitary(A)
    is_projection(A)
    Continue = input("\n'Yes' to check another matrix?sss: ")
    if Continue.lower() == 'yes':
        continue
    else:
        print("Exiting the program.")
        break