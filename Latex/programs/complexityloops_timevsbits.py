# import libraries
import math
import timeit
from matplotlib import pyplot as plt

def mod_exponentiation(bas, exp,N): # fast modular exponentiation
    if (exp == 0): 
        return 1; 
    if (exp == 1): 
        return bas % N; 
      
    t = mod_exponentiation(bas, int(exp / 2),N); 
    t = (t * t) % N; 
      
    # if exponent is even value 
    if (exp % 2 == 0): 
        return t; 
          
    # if exponent is odd value 
    else: 
        return ((bas % N) * t) % N;

def generate_nbit_int(n):
    bin_bits=[]
    for i in range(2**(n-1),2**(n)):
        bin_bits.append(i)
    return bin_bits

def find_coprime(N):
    for i in range(2,N+1):
        if N%i!=0:
            return i

def find_loop(N, coprime):
    w=0
    lo=0
    if N%coprime==0:
        raise Exception('{} and given {} are not coprime'.format(N,coprime))
    return math.ceil(math.sqrt(N)) # retun N for longer loop period(brute force method)
    for i in range(1,math.ceil(math.sqrt(N)+1)):
        # w=mod_exponentiation(coprime,i,N)  # to use fast exponentiation
        w=math.pow(coprime,i,N)
        lo=lo+1
        if w==1:
        return i
        break

def generate_num_loops(bits):
    loop=[]
    for num in bits:
        coprime=find_coprime(num)
        temp=find_loop(num,coprime)
        loop.append(temp)
    return max(loop)

def loops_timevsbits(max_bits):
    range_bits=[2**i for i in range(2,max_bits)]
    num_loops=[]
    total_time=[]
    for i in range(1,len(range_bits)):
        tic = timeit.default_timer()
        loop =  generate_num_loops(range(range_bits[i-1],range_bits[i]))
        toc=timeit.default_timer()
        num_loops.append(loop)
        total_time.append(toc-tic)
  
    return num_loops,total_time

bitlength=30
loops_taken,time_taken=loops_timevsbits(bitlength) # find number of loops and time taken to find the loops
# print(a,b)

"""For ploting graph """
bit=range_bits=[i for i in range(3,m)]
# plot number of loops versus bit length

plt.figure(figsize=(12,8))
plt.style.use('seaborn-whitegrid')
plt.xlabel('Bit length')
plt.ylabel('Numbers of loops required')
plt.plot(bit,loops_taken)  #  ,'r-o'
plt.bar(bit,loops_taken,width=0.8,tick_label=bit)
# plt.savefig('num_loops_vs_bits.png')
plt.show()

# plot time taken versus bit length

plt.figure(figsize=(12,8))
plt.style.use('seaborn-whitegrid')
plt.xlabel('Bit length')
plt.ylabel('Time taken to find period (in seconds)')
plt.plot(bit,time_taken)
plt.bar(bit,time_taken,width=0.8,tick_label=bit)
# plt.savefig('time_period_vs_bits.png')
plt.show()
