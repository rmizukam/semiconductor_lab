import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PlotFitMacros import roughPlt
import math
# testing the code to make sure it works on a resistor
psr = pd.read_csv('PSOhmic.txt',delimiter='\t',header=None)
p1 = plt.figure(1,figsize=(9,5))
plt.xlabel('$V_s$ [V]', fontsize = 12)
plt.ylabel('I [mA]', fontsize = 12)
plt.plot(psr[0][:],psr[1][:], 'r')


psi = pd.read_csv('PSI.txt',delimiter='\t',header=None)
ps3as1=pd.read_csv('PS3AS1.txt',delimiter='\t',header=None)
ps3bs1=pd.read_csv('PS3BS1.txt',delimiter='\t',header=None)
ps3bs2=pd.read_csv('PS3BS2.txt',delimiter='\t',header=None)

p2 = plt.figure(2, figsize=(9,5))
plt.subplot(1,2,1)
plt.xlabel('$V_s$ [V]', fontsize = 12)
plt.ylabel('I [mA]', fontsize = 12)
plt.plot(psi[0][:], psi[1][:], 'r', label='Instructor Sample')
plt.plot(ps3as1[0][:], ps3as1[1][:], 'c', label='3A Sample 1')
plt.plot(ps3bs1[0][:], ps3bs1[1][:], 'g', label='3B Sample 1')
plt.plot(ps3bs2[0][:], ps3bs2[1][:], 'y', label='3B Sample 2')
plt.grid(True, which='both')
plt.legend()
plt.subplot(1,2,2)
plt.xlabel('$V_s$ [V]', fontsize = 12)
plt.ylabel('I [mA]', fontsize = 12)
plt.plot(psi[0][0:13], psi[1][0:13], 'r', label='Instructor Sample')
plt.plot(ps3as1[0][0:13], ps3as1[1][0:13], 'c', label='3A Sample 1')
plt.plot(ps3bs1[0][0:13], ps3bs1[1][0:13], 'g', label='3B Sample 1')
plt.plot(ps3bs2[0][0:13], ps3bs2[1][0:13], 'y', label='3B Sample 2')
plt.grid(True,which='both')
plt.show()
