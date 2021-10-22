
import numpy as np

def areCospectral(A, B):
    """Input: 2 quadratic matrices of size n. Output: True/False depending if A and B are cospectral."""

    A_evals, _ = np.linalg.eig(A) # A_evecs
    B_evals, _ = np.linalg.eig(B) # B_evecs

    cospectral = validateEigenvalues(A_evals, B_evals)

    if cospectral:
        return True
    else:
        return False

def validateEigenvalues(A_evals, B_evals, err = 2 ** (-20)):
    """Input: 2 vectors containing the eigenvalues of 2 matrices. 
    Output: True if the difference in all values is smaller then a given error."""
    
    evals = []

    for i in range(len(A_evals)):
        if A_evals[i] - B_evals[i] > err:
            return False
        evals.append(round(A_evals[i], 2))
    print(evals)

    return True

A = [
    [0,0,1,0,1],
    [0,0,0,0,0],
    [1,0,0,1,0],
    [0,0,1,0,1],
    [1,0,0,1,0]
]

B = [
    [0,1,0,0,0],
    [1,0,1,1,1],
    [0,1,0,0,0],
    [0,1,0,0,0],
    [0,1,0,0,0]
]

print(areCospectral(A, B))