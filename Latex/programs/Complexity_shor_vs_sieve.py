""" Code to plot the graph  showing complexity of Shor’s algorithm and number field seive"""

# import necessary packages
import math
import matplotlib.pyplot as plt

x=[i for i in range(4,500)]
# y1=[ 1.9*math.pow(i,3) for i in x[1:]]
y1 = [math.pow(2,(1.9*math.log2(math.pow(n,1/3))*math.log2(math.pow(math.log2(n),2/3)))) for n in x]
y2=[math.log2(math.pow(n,3)) for n in x]

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(14,8))
plt.xlabel('number of bits')
plt.ylabel('Numbers of operations in log scale')
plt.plot(x,y1)
plt.plot(x,y2)
plt.yscale("log")
plt.annotate(text='Number seive',xy=(300,1400), xytext=(280,2500), 
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3"))
plt.annotate(text='Shor algorithm',xy=(300,25), xytext=(280,50), 
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3"))
plt.savefig('Complexity_shor_vs_sieve.png')