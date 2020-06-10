import math

def f(x):
    return (-1)**(x)*(3.0)**(2*x+1)/math.factorial(2*x+1)

n=int(input("What is the value of n?"))

partsum=0
i=0

while (i<=n):
    partsum=partsum + f(i)
    print(i,f(i),partsum)
    i=i+1
    
print("The partial sum is ", partsum)
