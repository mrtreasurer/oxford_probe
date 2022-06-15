import numpy as np
import pathlib

from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq

# dp = pathlib.Path("C:/Users/bhlvandenabbee/surfdrive/Data/20220428_oxfordprobe")
dp = pathlib.Path("C:/Users/bhlvandenabbee/OneDrive - Delft University of Technology/TWMTDWBF -DCSC/DataLabView")

# files = ["20220525-161631_COM7.csv"]
# speed = [9e-3]

files = ["Book7.csv", "Book8.csv", "Book9.csv"]
speed = [1/2e3, 1/1.8e3, 1/3e3]

for fi, f in enumerate(files):
    fp = dp / f
    data = np.genfromtxt(fp, delimiter=",")

    fig, axes = plt.subplots(len(data[0]), 2)

    for i, ax in enumerate(axes):
        # ax[0].plot(data[:, 0] - data[0, 0], data[:, i+1])
        ax[0].plot(np.linspace(0, speed[fi]*(len(data[:, i]) - 1), len(data[:, i])), data[:, i])
        ax[0].set_title(f"Signal {i+1}")
        ax[0].set_xlabel("Time [s]")
        ax[0].set_ylabel("Signal [V]")

        # ft_y = rfft(data[:, i+1] - np.mean(data[:, i+1]))
        ft_y = rfft(data[:, i] - np.mean(data[:, i]))
        ft_x = rfftfreq(len(data[:, i]), speed[fi])

        ax[1].plot(ft_x, np.abs(ft_y))
        ax[1].set_title(f"Fourier Transform Signal {i+1}")
        ax[1].set_xlabel("Frequency [Hz]")

plt.show()