import numpy as np


# Own implementation with the help of numpy

# np.array definition is in numpy: x = np.array[[1,2], [2,3]]

measurements = [1, 2, 3]

x = np.array([0., 0.]) # initial state (location and velocity)
P = np.array([[1000., 0.], [0., 1000.]]) # initial uncertainty
u = np.array([0., 0.]) # external motion
F = np.array([[1., 1.], [0, 1.]]) # next state function
H = np.array([[1., 0.]]) # measurement function
R = np.array([1.]) # measurement uncertainty
I = np.array([[1., 0.], [0., 1.]]) # identity np.array

########################################

# Implement the filter function below
       
def kalman_filter(x, P):
    for measurement in measurements:
        
        # measurement update
        Z = np.array([measurement])
        y = Z - H@x
        S = np.dot(np.dot(H,P),H.T) + R
        S_inv = np.linalg.inv(S)
        K = np.dot(np.dot(P,H.T),S_inv)
        x += np.dot(K,y.T)
        P = np.dot(I-np.dot(K,H), P)
        
        # prediction
        x = np.dot(F,x) + u
        P= np.dot(np.dot(F,P),F.T)
        
    return x,P


############################################
### use the code below to test your filter!
############################################



print(kalman_filter(x, P))
# output should be:
# x: [[3.9996664447958645], [0.9999998335552873]]