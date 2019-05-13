import numpy as np

design = np.array([[1,1],[1,2],[1,3]])

output = np.array([[1],[2],[3]])

tehta = np.array([[0],[1]])

def costFunc(X,y, theta):
    m = X.shape[0]
    hypo = np.dot(X,theta)
    costerr = (1/(2*m))*(hypo - y)**2
    return costerr

print(costFunc(design,output,tehta))