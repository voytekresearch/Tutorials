""" functions to create and plot noise"""
import numpy as np
from numpy.fft import irfft
import pandas as pd
import scipy as sp
from scipy.signal import normalize
import matplotlib.pyplot as plt
    
def noise_time_plot(data, time_scale):

    #plot 1 second of pink noise data
    plt.figure(figsize = [12,6])
    plt.plot(time_scale[0:1000], data[0:1000]) #plot samples over time
    
def noise_frequency_plot(fourier, fx_bins, title):
    # calculating fourier transform
    # we're going to take a sample of the data to keep fx bins at a reasonable size.
   
    plt.figure(figsize=(16,10))
    plt.subplot(1,2,1)
    plt.plot(fx_bins[0:1500],abs(fourier[0:1500])) 
    plt.ylabel('Power')
    plt.xlabel('Frequency (Hz)')
    plt.title(title)

    #same thing but in log space
    plt.subplot(1,2,2)
    plt.plot(fx_bins[0:1500],np.log(abs(fourier[0:1500]))) 
    plt.ylabel('log Power')
    plt.xlabel('Frequency (Hz)')
    plt.title(title) 
    
def welch_plot(fs, ps, title):
    #Welch's PSD of brown noise
   
    plt.figure(figsize=(16,10))
    plt.loglog(fs[0:200*2],ps[0:200*2])
    plt.ylabel('Power')
    plt.xlabel('Frequency (Hz)')
    plt.xlim([1, 150])
    plt.title(title)