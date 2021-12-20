import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PlotFitMacros import roughPlt,linErrPlt
from scipy.optimize import curve_fit
import math
def linFunc(x,b,m):
    y = b + m * x
    return y
kb = 8.617333262145e-5 # eV /K
kB = 1.380649e-23 # J/K
qe = 1.602176634e-19 # Coulomb

temps = [300,285,270,225,210]
ppmsr = pd.read_csv('1i+2i+RoomTemp.txt',delimiter='\t',header=None)
ppms285=pd.read_csv('1i+2i+285.txt',delimiter='\t',header=None)
ppms270=pd.read_csv('1i+2i+270.txt',delimiter='\t',header=None)
ppms255=pd.read_csv('1i+2i+255.txt',delimiter='\t',header=None)
ppms240=pd.read_csv('1i+2i+240.txt',delimiter='\t',header=None)
ppms225=pd.read_csv('1i+2i+225.txt',delimiter='\t',header=None)
ppms210=pd.read_csv('1i+2i+210.txt',delimiter='\t',header=None)

p1 = plt.figure(1)
plt.xlabel('$V_S$ [V]', fontsize = 12)
plt.ylabel('I [mA]', fontsize = 12)
# plt.title('IV Curve at Different Temperatures', fontsize = 12)
plt.plot(ppmsr[0][:], ppmsr[1][:], 'r', label='300 K')
plt.plot(ppms285[0][:], ppms285[1][:], 'c', label='285 K')
plt.plot(ppms270[0][:], ppms270[1][:], 'g', label='270 K')
plt.plot(ppms255[0][:], ppms255[1][:], 'y', label='255 K')
plt.plot(ppms240[0][:], ppms240[1][:], 'm', label='240 K')
# plt.plot(ppms225[0][:], ppms225[1][:], 'b', label='225 K')
# plt.plot(ppms210[0][:], ppms210[1][:], 'orange', label='210 K')
plt.legend()

# p2 = plt.figure(2)
# plt.xlabel('$1/T$ $[1/K]$', fontsize = 12)
# plt.ylabel('$ln(I/T^2)$', fontsize = 12)
# plt.title('Energy Barrier for Semiconductor', fontsize = 12)

x = np.divide(1,temps)
yy = [ppmsr[1][4],ppms285[1][4],ppms270[1][4],ppms225[1][4],ppms210[1][4]]
# print(yy)
yy = np.multiply(yy,1e-3)
# print(yy)
yerr = np.multiply(0.001, np.ones(len(yy)))

temp2 = np.multiply(temps,temps)
yy = np.divide(yy,temp2)
# print(yy)
yy = np.multiply(yy,-1)
for t in range(0,len(yy)):
    yy[t] = np.log(yy[t])

p2 = plt.figure(2)
plt.xlabel('$1/T$ $[1/K]$', fontsize = 12)
plt.ylabel('$ln(I/T^2)$', fontsize = 12)
plt.title('Energy Barrier for Semiconductor', fontsize = 12)
plt.errorbar(x,yy,yerr,fmt='.',c='c')
ans, cov = curve_fit(linFunc, x, yy, sigma = yerr)
fit_b = ans[0]
fit_m = ans[1]
fit_x_span = np.arange(0.003,0.005,0.0001)
del_fit_b = math.sqrt(cov[0][0])
del_fit_m = math.sqrt(cov[1][1])
plt.plot(fit_x_span, linFunc(fit_x_span, fit_b, fit_m), 'r')
delta_function = (-(fit_m)*kB)/qe
delta_function_2 = (-(fit_m)*kB)
dfunc = (-(fit_m)*kb)/qe
dfunc_2 = (-(fit_m)*kb)
# print(fit_m)
print(delta_function)
print(delta_function_2)
print(dfunc)
print(dfunc_2)



# plt.close(p1)
# plt.close(p2)
plt.show()
