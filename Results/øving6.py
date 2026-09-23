import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime,timezone


#Del1
t = np.linspace(0, 24, 500)

A = 800
mu = 13.5
sigma = 4

G = A * np.exp(-(t - mu)**2 / (2 * sigma**2))
G_max = np.max(G)

plt.plot(t, G)
plt.xlabel("Tid [timer]")
plt.ylabel("Innstråling [W/m²]")
plt.xticks(np.arange(0, 25, 1))
plt.grid()
plt.legend()
plt.plot(t, G_max * np.ones_like(t), "r--", label="Maksimal innstråling")
plt.legend()
plt.show()

#Del2