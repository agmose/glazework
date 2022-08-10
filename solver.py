import numpy as np

#We will take a linear (i.e., Ax = b) modeling approach to solve our equation :-x[0] + x[1]*ln(M) = b :

M = np.log([10.80000,28.20000,70.70000,105.00000])
A = np.vstack((-np.ones(M.size),M))
b = np.array([23.84950,28.31647,32.59418,34.43983])
x = np.linalg.lstsq(A.transpose(),b)[0]
