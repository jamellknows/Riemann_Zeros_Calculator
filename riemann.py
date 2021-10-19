"Code for calculating all the no trivial zeros of the Riemann Hypothesis"
"Created by Jamell Samuels"
def riemann(number = 20):
    print('Be aware that zeros come in twos so for ' + str(number) + ' you have ' + str(number*2) + ' zeros.')
    number = number + 1
    print("Hello")
    import math
    import pandas as pd
    import numpy as np
    import csv
    l =[]
    k = []    
    x = list(range(0,number))
    theta = math.pi/3
    for elem in x:
        y = (math.pi/3)*(1+6*elem)
        y = math.sqrt((y**2/theta**2)-0.25)
        print(y)
        l.append(y) #"The first half of zeros"
        z = (5*math.pi/3)*(1+6/5*elem)
        z = math.sqrt((z**2/theta**2)-0.25)
        k.append(z) #"The second half of zeros"
        print(z)


    m = l + k
    m.sort()
    length = len(m)
    lenghtP = list(range(1,length+1))
    print("making file")
    df = pd.DataFrame(data={"zero":lenghtP, "value": m})
    df.to_csv("./riemann_zeros.csv", sep=',',index=False)
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







