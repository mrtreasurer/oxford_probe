import numpy as np
import pathlib

from matplotlib import pyplot as plt

for n in ["COM6"]:
    file_path1 = pathlib.Path(__file__).parent / f"data/20220420-153528_{n}.csv"
    data1 = np.genfromtxt(file_path1, delimiter=",")

    plt.figure()
    plt.title(n)
    plt.plot(data1[100:, 0] - data1[0, 0], data1[100:, 1:])

plt.show()
