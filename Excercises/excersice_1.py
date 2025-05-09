#For this problem, you aren't writing any code.
#Instead, please just change the last argument 
#in f() to maximize the output.

from math import *

def gauss_function(mu, sigma2, x):
    return 1/sqrt(2.*pi*sigma2) * exp(-.5*(x-mu)**2 / sigma2)

if __name__ == "__main__":
    print(f"Functional value for argument is f={gauss_function(10.,4.,10)}") #Change the 8. to something else!