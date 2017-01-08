import matplotlib.pyplot as plt

def plot(x, y):
    """
    Plot (x,y) using Matplotlib

    """
    fig, ax = plt.subplots(1)
    ax.plot(x, y, lw=2, label='walker position', color='blue')
    ax.set_xlabel('# People')
    ax.set_ylabel('Interaction')
    ax.grid()
    plt.show()
