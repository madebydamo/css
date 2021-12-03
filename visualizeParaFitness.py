import numpy as np
import sys
import matplotlib.pyplot as plt

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filepath = sys.argv[1]

        array = np.load(filepath, allow_pickle=True)

        if array.ndim == 3:
            for i in range(0, array.shape[2]):
                x_axis = np.linspace(0, array.shape[0], array.shape[0])
                y_axis = np.zeros(array.shape[0])
                for j in range(0, array.shape[0]):
                    y_axis[j] = array[j][0][i]
                plt.plot(x_axis, y_axis)
        else:
            x_axis = np.linspace(0, array.shape[0], array.shape[0])
            plt.plot(x_axis, array)

        plt.show()
