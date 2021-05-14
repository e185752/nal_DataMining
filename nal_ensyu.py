import matplotlib
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

import matplotlib.pyplot as plt
import numpy as np

def true_fanction(x):
    '''
    >>> true_fanction(0.0)
    0.0
    '''
    return np.sin(np.pi * x * 0.8) * 10


x = np.linspace(-1, 1, 500)
plt.plot(x,true_fanction(x))
plt.show()



if __name__ == "__main__":
    import doctest
    doctest.testmod()