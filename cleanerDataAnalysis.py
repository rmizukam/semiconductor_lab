import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PlotFitMacros import roughPlt,linErrPlt,uncertinMean
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

p1 = plt.figure(1,figsize=(10.5,5))
plt.subplot(1,2,1)
plt.xlabel('$V_s$ [V]', fontsize = 12)
plt.ylabel('I [mA]', fontsize = 12)
plt.title('A', fontsize = 12)
plt.plot(ppmsr[0][:], ppmsr[1][:], 'r', label='300 K')
plt.plot(ppms285[0][:], ppms285[1][:], 'c', label='285 K')
plt.plot(ppms270[0][:], ppms270[1][:], 'g', label='270 K')
plt.plot(ppms255[0][:], ppms255[1][:], 'y', label='255 K')
plt.plot(ppms240[0][:], ppms240[1][:], 'm', label='240 K')
plt.grid(True,which='both')
# plt.plot(ppms225[0][:], ppms225[1][:], 'b', label='225 K')
# plt.plot(ppms210[0][:], ppms210[1][:], 'orange', label='210 K')
plt.legend()
plt.subplot(1,2,2)
plt.xlabel('$V_s$ [V]', fontsize = 12)
plt.ylabel('I [mA]', fontsize = 12)
plt.title('B', fontsize = 12)
plt.plot(ppmsr[0][0:16], ppmsr[1][0:16], 'r', label='300 K')
plt.plot(ppms285[0][0:16], ppms285[1][0:16], 'c', label='285 K')
plt.plot(ppms270[0][0:16], ppms270[1][0:16], 'g', label='270 K')
plt.plot(ppms255[0][0:16], ppms255[1][0:16], 'y', label='255 K')
plt.plot(ppms240[0][0:16], ppms240[1][0:16], 'm', label='240 K')
plt.grid(True,which='both')

def phiHeight(fig_num,k,title):
    temps = [300,285,270,240]
    x = np.divide(1,temps)
    yy=np.multiply([ppmsr[1][k],ppms285[1][k],ppms270[1][k],ppms240[1][k]],1e-3)
    yerr=np.multiply(5e-8, np.ones(len(yy)))
    temp2=np.multiply(temps,temps)
    yy=np.divide(yy,temp2)
    yy=np.multiply(yy,-1)
    for t in range(0,len(yy)):
        yy[t] = np.log(yy[t])
    fig_name=plt.figure(fig_num)
    plt.xlabel('$1/T$ $[1/K]$', fontsize = 12)
    plt.ylabel('$ln(I/T^2)$', fontsize = 12)
    plt.title(title, fontsize = 12)
    plt.errorbar(x,yy,yerr,fmt='.',c='c')
    # plt.xticks()
    ans,cov=curve_fit(linFunc, x, yy, sigma = yerr)
    fit_b=ans[0]
    fit_m=ans[1]
    fit_x_span=np.arange(0.0032,0.0045,0.0001)
    del_fit_b=math.sqrt(cov[0][0])
    del_fit_m=math.sqrt(cov[1][1])
    plt.plot(fit_x_span,linFunc(fit_x_span,fit_b,fit_m),'r')
    phi=(-(fit_m)*kb)
    return fig_name, phi


p2, phi1 = phiHeight(2,0,'V = -5 V') # @ -5V (-4.99675000 V)
p3, phi2 = phiHeight(3,3,'T = -4.7 V') # @ -4.7V
p4, phi3 = phiHeight(4,5,'T = -4.5 V K') # @ -4.5V

print(phi1)
print(phi2)
print(phi3)
meanphi = np.mean([phi1,phi2,phi3])
dmeanphi = uncertinMean([phi1,phi2,phi3])
print('SB Barrier = ', meanphi, ' +/- ', dmeanphi)
# 0.35 +/- 0.04 eV


#end of actual analysis, making graphs for report/ presentation
#
# k=0
# temps = [300,285,270,240]
# x = np.divide(1,temps)
# yy=np.multiply([ppmsr[1][k],ppms285[1][k],ppms270[1][k],ppms240[1][k]],1e-3)
# yerr=np.multiply(5e-8, np.ones(len(yy)))
# temp2=np.multiply(temps,temps)
# yy=np.divide(yy,temp2)
# yy=np.multiply(yy,-1)
# for t in range(0,len(yy)):
#     yy[t] = np.log(yy[t])
# p5=plt.figure(5)
# plt.subplot(2,2,1)
# plt.xlabel('$1/T$ $[1/K]$', fontsize = 12)
# plt.ylabel('$ln(I/T^2)$', fontsize = 12)
# # plt.title(title, fontsize = 12)
# plt.errorbar(x,yy,yerr,fmt='.',c='c')
# # plt.xticks()
# ans,cov=curve_fit(linFunc, x, yy, sigma = yerr)
# fit_b=ans[0]
# fit_m=ans[1]
# fit_x_span=np.arange(0.0032,0.0045,0.0001)
# del_fit_b=math.sqrt(cov[0][0])
# del_fit_m=math.sqrt(cov[1][1])
# plt.plot(fit_x_span,linFunc(fit_x_span,fit_b,fit_m),'r')
#
# k=3
# yy=np.multiply([ppmsr[1][k],ppms285[1][k],ppms270[1][k],ppms240[1][k]],1e-3)
# yerr=np.multiply(5e-8, np.ones(len(yy)))
# yy=np.divide(yy,temp2)
# yy=np.multiply(yy,-1)
# for t in range(0,len(yy)):
#     yy[t] = np.log(yy[t])
# plt.subplot(2,2,2)
# plt.xlabel('$1/T$ $[1/K]$', fontsize = 12)
# plt.ylabel('$ln(I/T^2)$', fontsize = 12)
# # plt.title(title, fontsize = 12)
# plt.errorbar(x,yy,yerr,fmt='.',c='c')
# # plt.xticks()
# ans,cov=curve_fit(linFunc, x, yy, sigma = yerr)
# fit_b=ans[0]
# fit_m=ans[1]
# fit_x_span=np.arange(0.0032,0.0045,0.0001)
# del_fit_b=math.sqrt(cov[0][0])
# del_fit_m=math.sqrt(cov[1][1])
# plt.plot(fit_x_span,linFunc(fit_x_span,fit_b,fit_m),'r')
#
# k=5
# yy=np.multiply([ppmsr[1][k],ppms285[1][k],ppms270[1][k],ppms240[1][k]],1e-3)
# yerr=np.multiply(5e-8, np.ones(len(yy)))
# yy=np.divide(yy,temp2)
# yy=np.multiply(yy,-1)
# for t in range(0,len(yy)):
#     yy[t] = np.log(yy[t])
# plt.subplot(2,2,3)
# plt.xlabel('$1/T$ $[1/K]$', fontsize = 12)
# plt.ylabel('$ln(I/T^2)$', fontsize = 12)
# # plt.title(title, fontsize = 12)
# plt.errorbar(x,yy,yerr,fmt='.',c='c')
# # plt.xticks()
# ans,cov=curve_fit(linFunc, x, yy, sigma = yerr)
# fit_b=ans[0]
# fit_m=ans[1]
# fit_x_span=np.arange(0.0032,0.0045,0.0001)
# del_fit_b=math.sqrt(cov[0][0])
# del_fit_m=math.sqrt(cov[1][1])
# plt.plot(fit_x_span,linFunc(fit_x_span,fit_b,fit_m),'r')
# p6 = plt.figure(6,figsize=(12,9))
# plt.xlabel('$V_s$ [V]', fontsize = 12)
# plt.ylabel('I [mA]', fontsize = 12)
# plt.title('PPMS Data At Various Temperatures', fontsize = 12)
# plt.plot(ppmsr[0][:], ppmsr[1][:], 'r', label='300 K')
# plt.plot(ppms285[0][:], ppms285[1][:], 'c', label='285 K')
# plt.plot(ppms270[0][:], ppms270[1][:], 'g', label='270 K')
# plt.plot(ppms255[0][:], ppms255[1][:], 'y', label='255 K')
# plt.plot(ppms240[0][:], ppms240[1][:], 'm', label='240 K')
# plt.grid(True,which='both')
# plt.legend()



# print(phi1)
# print(phi2)
# print(phi3)

plt.show()
