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
