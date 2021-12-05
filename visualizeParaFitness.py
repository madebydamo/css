import numpy as np
import sys
import matplotlib.pyplot as plt

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filepath = sys.argv[1]

        array = np.load(filepath, allow_pickle=True)

        if array.ndim == 3:
            parameterNames = [r'interaction strength A $f_{\alpha\beta}$',r'interaction range B of $f_{\alpha\beta}$',r'relaxation time $\tau$',r'interaction strength A $f_{\alpha i}$',r'interaction range B of $f_{\alpha i}$']
            for i in range(0, array.shape[2]):
                x_axis = np.linspace(0, array.shape[0], array.shape[0])
                y_axis = np.zeros(array.shape[0])
                for j in range(0, array.shape[0]):
                    y_axis[j] = array[j][0][i]
                plt.plot(x_axis, y_axis,label=parameterNames[i])
        else:
            x_axis = np.linspace(0, array.shape[0], array.shape[0])
            plt.plot(x_axis, array)
        plt.legend(loc='best')
        plt.xlabel('Generations')
        plt.ylabel('Parameter Value')
        plt.show()
