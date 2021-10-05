
'''Installation of some necessary packages'''
# !pip install qiskit   # install qiskit package
# !pip install pylatexenc
# # the output will be cleared after installation
# from IPython.display import clear_output
# clear_output()



'''Shor's algorithm for composite number composed of fermat primes'''
# Import necessary packages
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
import numpy as np
import math

pi = math.pi



'''Import qiskit modules and functions'''
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute,Aer, IBMQ
from qiskit.visualization import plot_histogram
from qiskit.compiler import transpile, assemble
from qiskit.quantum_info import state_fidelity



''' Function to construct circuit for Quantum Fourier Transform 
and inverse Quantum Fourier transform'''
def create_qft(qc, q_reg, n_qubit, swap=True, inverse=False,approx=0):
    pi= math.pi
    if inverse:
        if swap:
            for q in range(int(n_qubit/2)):
                qc.swap(q_reg[q],q_reg[n_qubit-q-1])
        for i in range(n_qubit):
            for j in range(i):
                qc.cp(-pi/math.pow(2,(i-j)), q_reg[j], q_reg[i])
            qc.h(q_reg[i])
            qc.barrier()
        
        
    else:
        for i in range(n_qubit-1,-1,-1):
            qc.h(q_reg[i])
            for j in range(i-1,-1,-1):
                if(pi)/(pow(2,(i-j)))>0:
                    qc.cp(pi/math.pow(2,(i-j)), q_reg[i], q_reg[j])
                    
            
            qc.barrier()
           
        if swap:
            for q in range(int(n_qubit/2)):
                qc.swap(q_reg[q],q_reg[n_qubit-q-1])


'''Preparation of Quantum circuit'''
in_qreg = QuantumRegister(4,'inp')  # create input register
per_qreg = QuantumRegister(2,'per')  # create period register
creg = ClassicalRegister(4,'clas')  # create classical register

qc = QuantumCircuit(in_qreg, per_qreg, creg) #  initialize a quantum circuit

# Create superposition using hadamard gate
qc.h(in_qreg)
qc.barrier()  # add barrier to make the circuit representation clear

# Apply compiled modular exponentiation function between two register
qc.cx(in_qreg[0],per_qreg[0])
qc.cx(in_qreg[1],per_qreg[1])
qc.barrier()  # add barrier to make the circuit representation clear

# Apply inverse quantum fourier transformon input register
create_qft(qc, in_qreg, 4, swap=True, inverse=True)  # swap=False to omit swap operation

# apply measurement on input register and collapse to classical register
qc.measure(in_qreg, creg)

qc.draw(output = 'mpl',filename = 'shorfor15_2.png', scale = 3)



'''Run the circuit in simulator: '''
# Load saved IBMQ account
# IBMQ.save_account("*********************************************************************************************************************************")

IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q')
sim_backend = provider.get_backend("ibmq_qasm_simulator")
'''import least busy quantum backend'''
from qiskit.providers.ibmq import least_busy
n=6
qc_backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= n 
                                       and not x.configuration().simulator 
                                       and x.status().operational==True))
print("least busy quantum backend: ", qc_backend)


"""Run the circuit in Processers: Use backend='sim_backend' for simulator
s and backend= 'qc_backend' for quantum coputers  """

# running circuit on simulator at IBM
job = execute(qc,backend=sim_backend,shots =8000 )
result = job.result()
counts=result.get_counts(qc)
counts


fig,ax = plt.subplots(figsize=(12,8))  # figsize=(16,8)
ax.set_aspect('auto')
plot_histogram(counts,ax=ax)
plt.savefig('histogram_result_fermat_sim.png',dpi=800)


# running circuit on quantum computer
job_qc = execute(qc,backend=qc_backend,shots =8000 )
result_qc = job_qc.result()
counts_qc=result_qc.get_counts(qc)
counts_qc


fig,ax = plt.subplots(figsize=(12,8))  # figsize=(16,8)
ax.set_aspect('auto')
plot_histogram(counts_qc,ax=ax)
plt.savefig('histogram_result_fermat_qc.png',dpi=800)




import qiskit
qiskit.__qiskit_version__

{'qiskit-terra': '0.16.2',
 'qiskit-aer': '0.7.3',
 'qiskit-ignis': '0.5.1',
 'qiskit-ibmq-provider': '0.11.1',
 'qiskit-aqua': '0.8.1',
 'qiskit': '0.23.3'}
