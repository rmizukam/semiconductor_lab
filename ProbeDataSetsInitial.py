import pandas as pd
import matplotlib.pyplot as plt
import math

negIns1 = pd.read_csv('negative_instructor_1.txt',delimiter="\t",header=None)
posIns1 = pd.read_csv('positive_instructor_1.txt',delimiter="\t",header=None)

voltage = negIns1[0][:] + posIns1[0][:]
current = negIns1[1][:] + posIns1[1][:]

plt.figure(figsize=(12,8))
plt.xlabel('Voltage [V]', fontsize = 16)
plt.ylabel('Current [A]', fontsize = 16)
plt.title('Initial Probe Station IV Curve', fontsize = 18)
plt.xscale('linear')
plt.yscale('linear')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.plot(voltage,current,c='r', marker='o',linestyle='None',markersize=4)
plt.show()
