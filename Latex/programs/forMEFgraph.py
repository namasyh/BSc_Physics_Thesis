""" Code to plot Modular exponentiation function outputs of two types """

#import necessary packages
%matplotlib inline
import matplotlib.pyplot as plt 
plt.style.use('seaborn-notebook')
# plt.style.available
import numpy as np
from scipy.fft import fft

def gcd(a,b):
'''   return the greatest common divisor of a,b'''
    while (b):
      m = a % b
      a = b
      b = m
    return a

def periodfind(x,I,N):  
    '''find period a of function f(x)=x^a mod N '''
    arr=[]
    for i in range(N):
        f= (x**i)%(I)
        arr.append(f)
    return arr

'''For case I'''
N=16
I=16
z=3
y=np.array(periodfind(z,I,N))
x=np.arange(N)
plt.style.use('seaborn-whitegrid')
plt.title('Period of function f(x)=${}^x$(mod {I})'.format(z,I=I))
plt.xlabel('x')
plt.ylabel('f(x)=${}^x$(mod {I})'.format(z,I=I))
plt.plot(x,y,'o',linewidth=1)  #  ,'r-o'
plt.plot(x,y,'--')
plt.show()


'''For caseII'''
N=15
I=15
z=2
y=np.array(periodfind(z,I,N))
x=np.arange(N)
plt.style.use('seaborn-whitegrid')
plt.title('Period of function f(x)=${}^x$(mod {I})'.format(z,I=I))
plt.xlabel('x')
plt.ylabel('f(x)=${}^x$(mod {I})'.format(z,I=I))
plt.plot(x,y,'o',linewidth=1)  #  ,'r-o'
plt.plot(x,y,'--')
plt.show()

