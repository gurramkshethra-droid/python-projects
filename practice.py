import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x=np.array([2023,2024,2025,2026])
y1=np.array([22,25,30,20])
y2=np.array([17,23,25,13])

plt.plot(x,y1,marker=".",
         ms=30,
         mfc="#03fcf0",
         linestyle="dotted",
         linewidth=4,
         color="#fc03c6")

plt.plot(x,y2,marker=".",
         ms=30,
         mfc="#03fcf0",
         linestyle="dashed",
         linewidth=4,
         color="#b103fc")

plt.show()