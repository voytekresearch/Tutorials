""" functions to create and plot noise"""
import numpy as np
from numpy.fft import irfft
import pandas as pd
import scipy as sp
from scipy.signal import normalize
import matplotlib.pyplot as plt

def white_noise_time():
    #Generate white noise time series 
    mean = 0
    std = 1 

    # length of time series
    num_samples = 1000000 

    # sampling rate 1000Hz
    fs = 1000 

    # generate white (random) noise
    white_noise_data = np.random.normal(mean, std, size=num_samples) 

    # time scale = number of samples / sampling rate
    t = np.arange(len(white_noise_data))/fs 

    #p lot 1 second of white noise data
    plt.figure(figsize=[12,6])
    plt.plot(t[0:1000], white_noise_data[0:1000]) #plot samples over time
    return white_noise_data,fs
    
def white_noise_frequency(white_noise_data,fs):
    # calculating fourier transform of complex signal
    # we're going to take a sample of the data to keep fx bins at a reasonable size.
    fourier = np.fft.fft(white_noise_data[0:10000]) 

    # finding frequency values for the x axis
    fx_step_size = fs/len(white_noise_data[0:10000])
    nyq = .5*fs
    total_steps = nyq/fx_step_size
    fx_bins = np.linspace(0,nyq,total_steps)

    plt.figure(figsize=(16,10))
    plt.subplot(1,2,1)
    plt.plot(fx_bins[0:4000],abs(fourier[0:4000])) #any frequencies above 200 Hz are probably noise
    plt.ylabel('Power')
    plt.xlabel('Frequency (Hz)')
    plt.title('FFT of White Noise')

    # Same thing but in log space
    plt.subplot(1,2,2)
    plt.plot(fx_bins[0:4000],np.log(abs(fourier[0:4000]))) #any frequencies above 200 Hz are probably noise
    plt.ylabel('log Power')
    plt.xlabel('Frequency (Hz)')
    plt.title('FFT of White Noise')
    
def white_welch(white_noise_data,fs):
    #Welch's PSD of white noise
    f,pspec = sp.signal.welch(white_noise_data, fs=fs, window='hanning', nperseg=2*fs, noverlap=fs/2, nfft=None, detrend='linear', return_onesided=True, scaling='density')

    plt.figure(figsize=(16,10))
    plt.loglog(f[0:200*2],pspec[0:200*2])
    plt.ylabel('Power')
    plt.xlabel('Frequency (Hz)')
    plt.xlim([1, 150])
    plt.title("Welch's PSD of ECoG signal")
    
def pink_noise_time():
    #Function to generate time series with properties of pink noise
    def voss(nrows, ncols=16):
        """Generates pink noise using the Voss-McCartney algorithm.

        nrows: number of values to generate
        rcols: number of random sources to add

        returns: NumPy array
        """
        array = np.empty((nrows, ncols))
        array.fill(np.nan)
        array[0, :] = np.random.random(ncols)
        array[:, 0] = np.random.random(nrows)

        # the total number of changes is nrows
        n = nrows
        cols = np.random.geometric(0.5, n)
        cols[cols >= ncols] = 0
        rows = np.random.randint(nrows, size=n)
        array[rows, cols] = np.random.random(n)

        df = pd.DataFrame(array)
        df.fillna(method='ffill', axis=0, inplace=True)
        total = df.sum(axis=1)

        return total.values
    pink_data = voss(1000000)
    fs = 1000
    t = np.arange(len(pink_data))/fs

    #plot 1 second of pink noise data
    plt.figure(figsize=[12,6])
    plt.plot(t[0:1000], pink_data[0:1000]) #plot samples over time
    
    return pink_data,fs
    
def pink_noise_frequency(pink_data,fs):
    # calculating fourier transform of complex signal
    # we're going to take a sample of the data to keep fx bins at a reasonable size.
    fourier = np.fft.fft(pink_data[0:10000]) 

    # finding frequency values for the x axis
    fx_step_size = fs/len(pink_data[0:10000])
    nyq = .5*fs
    total_steps = nyq/fx_step_size
    fx_bins = np.linspace(0,nyq,total_steps)

    plt.figure(figsize=(16,10))
    plt.subplot(1,2,1)
    plt.plot(fx_bins[0:1500],abs(fourier[0:1500])) 
    plt.ylabel('Power')
    plt.xlabel('Frequency (Hz)')
    plt.title('FFT of Pink Noise')

    #same thing but in log space
    plt.subplot(1,2,2)
    plt.plot(fx_bins[0:1500],np.log(abs(fourier[0:1500]))) 
    plt.ylabel('log Power')
    plt.xlabel('Frequency (Hz)')
    plt.title('FFT of Pink Noise')
    
def pink_welch(pink_data,fs):
    #Welch's PSD of pink noise
    f,pspec = sp.signal.welch(pink_data, fs=fs, window='hanning', nperseg=2*fs, noverlap=fs/2, nfft=None, detrend='linear', return_onesided=True, scaling='density')

    plt.figure(figsize=(16,10))
    plt.loglog(f[0:200*2],pspec[0:200*2])
    plt.ylabel('Power')
    plt.xlabel('Frequency (Hz)')
    plt.xlim([1, 150])
    plt.title("Welch's PSD of Pink Noise")
    
def brown_noise_time():
    #Function to generate time series with properties of brown noise
    def brown(N, state=None):

        state = np.random.RandomState() if state is None else state
        uneven = N%2
        X = state.randn(N//2+1+uneven) + 1j * state.randn(N//2+1+uneven)
        S = (np.arange(len(X))+1)# Filter
        y = (irfft(X/S)).real
        if uneven:
            y = y[:-1]
        return normalize(y,1)
    # get brown noise data as time series
    normalized_arrays = brown(1000000)
    brown_data= normalized_arrays[0]
    fs = 1000
    t = np.arange(len(brown_data))/fs

    #plot 1 second of brown noise data
    plt.figure(figsize=[12,6])
    plt.plot(t[0:1000], brown_data[0:1000]) #plot samples over time
    return brown_data, fs
    
def brown_noise_frequency(brown_data, fs):
    # calculating fourier transform of complex signal
    # we're going to take a sample of the data to keep fx bins at a reasonable size.
    fourier = np.fft.fft(brown_data[0:10000]) 

    # finding frequency values for the x axis
    fx_step_size = fs/len(brown_data[0:10000])
    nyq = .5*fs
    total_steps = nyq/fx_step_size
    fx_bins = np.linspace(0,nyq,total_steps)

    plt.figure(figsize=(16,10))
    plt.subplot(1,2,1)
    plt.plot(fx_bins[0:1500],abs(fourier[0:1500])) #any frequencies above 200 Hz are probably noise
    plt.ylabel('Power')
    plt.xlabel('Frequency (Hz)')
    plt.title('FFT of Brown Noise')

    plt.subplot(1,2,2)
    plt.plot(fx_bins[0:1500],np.log(abs(fourier[0:1500]))) #any frequencies above 200 Hz are probably noise
    plt.ylabel('log Power')
    plt.xlabel('Frequency (Hz)')
    plt.title('FFT of Brown Noise')
    
def brown_welch(brown_data, fs):
    #Welch's PSD of brown noise
    f,pspec = sp.signal.welch(brown_data, fs=fs, window='hanning', nperseg=2*fs, noverlap=fs/2, nfft=None, detrend='linear', return_onesided=True, scaling='density')

    plt.figure(figsize=(16,10))
    plt.loglog(f[0:200*2],pspec[0:200*2])
    plt.ylabel('Power')
    plt.xlabel('Frequency (Hz)')
    plt.xlim([1, 150])
    plt.title("Welch's PSD of Brown Noise")