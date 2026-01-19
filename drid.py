import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5]
y=[5,10,15,20,25]

plt.grid(axis="x",
         linewidth=2,
         color="lightgray",
         linestyle="dashdot")

plt.grid(axis="y",
         linewidth=3,
         color="lightgreen",
         linestyle="dotted")

plt.title("Grid Demo")
plt.plot(x,y)
plt.show()