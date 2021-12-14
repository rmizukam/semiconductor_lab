# PlottingAndFittingMacros
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import math


def linFunc(x,b,m):
    y = b + m * x
    return y

def linErrPlt(fig_num, title, xlabel, ylabel, xscale, yscale, xdata,\
        ydata, yerror, show_fit):
    fig_name= plt.figure(fig_num, figsize=(12,8))
    plt.xlabel(xlabel, fontsize = 12)
    plt.ylabel(ylabel, fontsize = 12)
    plt.title(title, fontsize = 12)
    plt.xscale(xscale)
    plt.yscale(yscale)
    plt.errorbar(xdata,ydata,yerror,fmt='.',c='c')
    ans, cov = curve_fit(linFunc, xdata, ydata, sigma = yerror)
    fit_b = ans[0]
    fit_m = ans[1]
    fit_x_span = np.arange((np.amin(xdata)), (np.amax(xdata)))
    del_fit_b = math.sqrt(cov[0][0])
    del_fit_m = math.sqrt(cov[1][1])
    if show_fit == 'y' or show_fit == 'yes':
        plt.plot(fit_x_span, linFunc(fit_x_span, fit_b, fit_m), 'r-')
    return fit_m, fit_b, del_fit_m, del_fit_b, fig_name

def errPropDiv(x,y,dx,dy):
    if type(x) == np.ndarray:
        array = [0] * len(x)
        for t in range(0, len(x)):
            array[t] = abs(x[t]/y[t]) * math.sqrt((dx[t]/x[t])**2 +\
                (dy[t]/y[t])**2)
        return array
    elif type(x) == int or type(x) == np.float64:
        return abs(x/y) * math.sqrt((dx/x)**2 + (dy/y)**2)
    else:
        print('You Passed Data Unusable For This Program')

def errPropMultiply(x, y, dx, dy):
    if type(x) == np.ndarray:
        array = [0]*len(x)
        for t in range(0,len(x)):
            array[t] = len(x[t]*y[t]) * math.sqrt((dx[t]/x[t])**2 +\
                (dy[t]/y[t])**2)
        return array
    elif type(x) == int or type(x) == np.float64:
        return abs(x*y) * math.sqrt((dx/x)**2 + (dy/y)**2)
    else:
        print('You Passed Data Unusable For This Program')

def errPropAddSubtract(dx,dy):
    if type(dx)== np.ndarray and type(dy)==np.ndarray:
        if len(dx) != len(dy):
            yy = [dy]*len(dx)
            array = [0]*len(dx)
            array = np.array(array)
        for t in range(0,len(dx)):
            xx = (dx[t])**2
            yy = (dy[t])**2
            array[t] = math.sqrt(xx + yy)
        return array
    elif type(dx) == np.ndarray and type(dy) == np.float64 or type(dy) == float:
         array = [dy] * len(dx)
         array = np.array(array)
         for t in range(0,len(dx)):
             xx = (dx[t])**2
             yy = (array[t])**2
             array[t] = math.sqrt(xx + yy)
         return array
    elif type(dx) != np.ndarray and type(dy) != np.ndarray:
        return math.sqrt(dx**2 + dy**2)

def errConst(c,x):
    return abs(c*x)

def errPow(x,dx,pow_factor):
    if type(x) == np.ndarray:
        array = [0]*len(x)
        for t in range(0,len(x)):
            array[t]
    elif type(x) == int or type(x) == np.float64:
        return abs(pow_factor) * x^(pow_factor - 1) * dx

def roughPlt(fig_num, title, xlabel, ylabel, xscale, yscale, xdata, ydata):
    fig_name= plt.figure(fig_num, figsize=(12,8))
    plt.xlabel(xlabel, fontsize = 12)
    plt.ylabel(ylabel, fontsize = 12)
    plt.title(title, fontsize = 12)
    plt.xscale(xscale)
    plt.yscale(yscale)
    plt.plot(xdata,ydata,'ro')
    return fig_name

def uncertinMean(data):
    return (np.amax(data) - np.amin(data)) / (2*math.sqrt(len(data)))
