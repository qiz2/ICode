#This Code test our DFA and Whittle function gives mean and var
#of the estimate Hurst exponent
import scipy.io as scio
import numpy as np
from ICode.Estimators import DFAS

f = scio.loadmat('ICode/simulations/simulationsfGn2.mat')

simulations = f['simulations']
#number of different h
n = simulations.shape[0]
#number of simulation for a given h
N = simulations.shape[1]
#length of simulation
l = simulations.shape[2]

dfai = np.zeros((n,N))

for i in np.arange(0,n):
  #We define anonymous functions that will be usefull
  d = lambda idx : DFAS(simulations[i,:,:],idx)
  #we lauch the threads !
  for j in range(N):
    dfai[i,j] = d(j)

  
s ='DFA'
f = open('ICode/simulations/Python_'+s+'_results','w')


    
  
if s == 'DFA':
  f.write('\n\n----------DFA-----------------------\n \n')
  f.write('Htheo\tH mean estimate for a fGn \t Var estimation\n')
  for i in np.arange(1,10):
    f.write(str(i) + '\t')

    f.write(str(np.mean(whittlei[i,:])) + '\t')
    
    f.write(str(np.var(whittlei[i,:])) + '\n')
    

  
f.close()
