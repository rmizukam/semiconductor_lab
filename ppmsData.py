import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PlotFitMacros import roughPlt

ppmsr = pd.read_csv('1i+2i+RoomTemp.txt',delimiter='\t',header=None)
ppms285=pd.read_csv('1i+2i+285.txt',delimiter='\t',header=None)
ppms270=pd.read_csv('1i+2i+270.txt',delimiter='\t',header=None)
ppms255=pd.read_csv('1i+2i+255.txt',delimiter='\t',header=None)
ppms240=pd.read_csv('1i+2i+240.txt',delimiter='\t',header=None)
ppms225=pd.read_csv('1i+2i+225.txt',delimiter='\t',header=None)
ppms210=pd.read_csv('1i+2i+210.txt',delimiter='\t',header=None)

p1 = plt.figure(1)
plt.xlabel('Voltage [V]', fontsize = 12)
plt.ylabel('Current [mA?]', fontsize = 12)
plt.title('IV Curve at Different Temperatures', fontsize = 12)
plt.plot(ppmsr[0][:], ppmsr[1][:], 'r', label='300 K')
plt.plot(ppms285[0][:], ppms285[1][:], 'c', label='285 K')
plt.plot(ppms270[0][:], ppms270[1][:], 'g', label='270 K')
plt.plot(ppms255[0][:], ppms255[1][:], 'y', label='255 K')
plt.plot(ppms240[0][:], ppms240[1][:], 'm', label='240 K')
plt.plot(ppms225[0][:], ppms225[1][:], 'b', label='225 K')
plt.plot(ppms210[0][:], ppms210[1][:], 'orange', label='210 K')

p2 = plt.figure(2)
plt.xlabel('1/T [1/K]', fontsize = 12)
plt.ylabel('ln(I/T)', fontsize = 12)
plt.title('Energy Barrier for Semiconductor', fontsize = 12)
x = [ppmsr[0][4],ppms285[0][4],ppms270[0][4],ppms240[0][4],ppms225[0][4],\
    ppms210[0][4]]
y = [np.log(ppmsr[1][4]),np.log(ppms285[1][4]),np.log(ppms270[1][4]),\
    np.log(ppms240[1][4]),np.log(ppms225[1][4]),np.log(ppms210[1][4])]

plt.plot(x,y,'r.')














plt.close(p1)
# plt.close(p2)
plt.legend()
plt.show()
