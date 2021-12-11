import pandas as pd
import matplotlib.pyplot as plt
import math
from PlotFitMacros import roughPlt

negIns1 = pd.read_csv('negative_instructor_1.txt',delimiter="\t",header=None)
posIns1 = pd.read_csv('positive_instructor_1.txt',delimiter="\t",header=None)
bbxNeg = pd.read_csv('breakOutBoxNeg.txt',delimiter="\t",header=None)
bbxPos = pd.read_csv('breakOutBoxPos.txt',delimiter='\t',header=None)
psNeg = pd.read_csv('probeStationNeg.txt',delimiter='\t',header=None)
psPos = pd.read_csv('probeStationPos.txt',delimiter='\t',header=None)


p1 =roughPlt(1, 'Instructor IV Curve', 'Voltage [V]', 'Current [A]','linear',\
    'linear', negIns1[0][:] + posIns1[0][:], negIns1[1][:] + posIns1[1][:])
p2 =roughPlt(2, 'Semiconductor Probe Station IV Curve', 'Voltage [V]', \
    'Current [A]','linear','linear', psNeg[0][:] + psPos[0][:], \
    psNeg[1][:] + psPos[1][:])
p3 =roughPlt(3, 'Semiconductor Breakout Box IV Curve', 'Voltage [V]', \
    'Current [A]','linear','linear', bbxNeg[0][:] + bbxPos[0][:], \
    bbxNeg[1][:] + bbxPos[1][:])

# plt.close(p1)
# plt.close(p2)
# plt.close(p3)
plt.show()
