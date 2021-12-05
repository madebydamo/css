import numpy as np
import sys
import matplotlib.pyplot as plt

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filepath = sys.argv[1]

        array = np.load(filepath, allow_pickle=True)

        if array.ndim == 3:
            parameterNames = [r'interaction strength A of $f_{\alpha\beta}$',r'interaction range B of $f_{\alpha\beta}$',r'relaxation time $\tau$',r'interaction strength A of $f_{\alpha i}$',r'interaction range B of $f_{\alpha i}$',r'Angle of encounter $\varphi$',r'prefactor $w$']
            for i in range(0, array.shape[2]):
                x_axis = np.linspace(0, array.shape[0], array.shape[0])
                y_axis = np.zeros(array.shape[0])
                for j in range(0, array.shape[0]):
                    y_axis[j] = array[j][0][i]
                plt.plot(x_axis, y_axis,label=parameterNames[i])
            plt.xlabel('Generations')
            plt.ylabel('Parameter Value') 
            plt.legend(loc='best')   
        else:
            fitnessNames = ['Destination Closeness','Collision Prevention']
            x_axis = np.linspace(0, array.shape[0], array.shape[0])
            colors = ['tab:blue','tab:orange']
            destinationFitness = array[:,0]
            collisionFitness = array[:,1]

            fig, ax1 = plt.subplots()
            ax1.set_xlabel('Generations')
            ax1.set_ylabel('Destination Closeness Fitness', color=colors[0])
            ax1.plot(x_axis, destinationFitness, color=colors[0])
            ax1.tick_params(axis='y', labelcolor=colors[0])

            ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
            ax2.set_ylabel('Collision Prevention Fitness', color=colors[1])  # we already handled the x-label with ax1
            ax2.plot(x_axis, collisionFitness, color=colors[1])
            ax2.tick_params(axis='y', labelcolor=colors[1])
            fig.tight_layout()

        plt.show()
