"Code for calculating all the no trivial zeros of the Riemann Hypothesis"
"Created by Jamell Samuels"
def riemann(number = 20):
    print('Be aware that zeros come in twos so for ' + str(number) + ' you have ' + str(number*2) + ' zeros.')
    number = number + 1
    import math
    import pandas as pd
    import numpy as np
    l =[]
    k = []    
    x = list(range(1,number))
    for elem in x:
        y = (math.pi/3)*(1+6*elem)
        print(y)
        l.append(y) #"The first half of zeros"
        z = (5*math.pi/3)*(1+6/5*elem)
        k.append(z) #"The second half of zeros"
        print(z)


    m = l + k
    m.sort()
    print(m)
    import matplotlib.pyplot as plt
    half = np.ones(len(m))
    half = half*0.5
    plt.figure()
    plt.plot(half,m, 'kx', half,m, 'r')
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.show()
    return m 







