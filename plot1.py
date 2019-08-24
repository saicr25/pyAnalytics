#myplot.py
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
x
np.sin(x)
#fig = plt.figure()
plt.plot(x, np.sin(x))
plt.savefig('plot1.png')
plt.savefig('E:/analytics/plots/plot1.png')# line 8 to 11 run together
plt.show(); # import when running from script

