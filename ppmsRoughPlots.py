import pandas as pd
import matplotlib.pyplot as plt
import math
from PlotFitMacros import roughPlt

ppmsr = pd.read_csv('1i+2i+RoomTemp.txt',delimiter='\t',header=None)
ppms285=pd.read_csv('1i+2i+285.txt',delimiter='\t',header=None)
ppms270=pd.read_csv('1i+2i+270.txt',delimiter='\t',header=None)

p1 =roughPlt(1, 'Semiconductor Breakout Box IV Curve', 'Voltage [V]', \
    'Current [A]','linear','linear', bbxNeg[0][:] + bbxPos[0][:], \
    bbxNeg[1][:] + bbxPos[1][:])
