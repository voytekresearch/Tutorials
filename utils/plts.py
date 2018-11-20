"""Tools and utilities for plotting."""

import matplotlib.pyplot as plt

from fooof.plts.templates import plot_spectrum

###################################################################################################
###################################################################################################

def plot_fm_shading(fm, cens, bws):
    """Plot a FOOOF power spectrum with shaded regions.

    Parameters
    ----------
    fm : FOOOF() object
        FOOOF object with power spectrum data to plot.
    cens : list of float
        List of center values to shade around.
    bws : list of float
        List of ranges to plot +/- each center regions.
    """

    plot_spectrum(fm.freqs, fm.power_spectrum)

    # Add shading +/- BW around each provided CEN.
    #  Note: m is a potential scaling of BW. Currently not-exposed (hard set to 1).
    m = 1
    for cen, bw in zip(cens, bws):
        plt.axvspan(cen, cen, color='g')
        plt.axvspan(cen-(m*bw), cen+(m*bw), color='r', alpha=0.2, lw=0)

    
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