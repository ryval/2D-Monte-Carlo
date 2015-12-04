# imports
import numpy as np

# globals
MAX_MCC = 100 # max number of monte carlo cycles
N = 100 # size of spin grid
T = 0.1 # temperature in energy units

# apply periodic boundary conditions
def pbc(i):
    if i >= N:
        return 0
    elif i < 0:
        return N - 1
    else:
        return i
        
# calculate the change in energy upon a spin flip at (i,j)
def delta_E(spins, i, j):
    return 2*spins[i][j] * (spins[pbc(i+1)][j]
                            + spins[pbc(i-1)][j]
                            + spins[i][pbc(j+1)]
                            + spins[i][pbc(j-1)])
        
# Initialize a random starting spin grid
def rand_spin():
    return np.random.randint(0, 2, size=(N,N)) * 2 - 1 
  
# An implementation of the metropolis algorithm
def metropolis(spins):
    # loop over all spins
    for i in range(0, N*N, 1):
        x = np.random.randint(0, N, size = 1)[0]
        y = np.random.randint(0, N, size = 1)[0]
        # find energy change if spin is flipped
        de = delta_E(spins, x, y)
        if de < 0: # if lower energy, flip the spin
            spins[x][y] *= -1
        elif np.exp(-de/T) > np.random.rand(): # flip spin
            spins[x][y] *= -1
    return spins

# Monte Carlo computation
def mc_relax(spins):
    for c in range(0, MAX_MCC, 1):
        spins = metropolis(spins)
    return spins
    
def __main__():   
    ispins = rand_spin()
    fspins = mc_relax(ispins)
    print fspins
    
if __name__ == "__main__":
    __main__()