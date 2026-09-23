import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime,timezone
import matplotlib.dates as mdates


#Del1
'''
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
'''

#Del2


df = pd.read_csv(
    "load/Timeseries_solar.csv",
    skiprows=8,
    nrows=17519
)
df["time"] = pd.to_datetime(
    df["time"],
    format="%Y%m%d:%H%M",
    utc=True
)
df = df.set_index("time")
df.index = df.index.round("h")


Sol_2023=df.loc["2023-01-01":"2023-12-31"]

plt.plot(Sol_2023.index, Sol_2023["G(i)"])
plt.xlabel("Tid")
plt.ylabel("Innstråling [W/m²]")
plt.show()

Sol_2023_06=Sol_2023.loc["2023-06-01":"2023-06-30"]
plt.plot(Sol_2023_06.index, Sol_2023_06["G(i)"])
plt.xlabel("Tid")
plt.ylabel("Innstråling [W/m²]")
plt.show()


sol_2023_08_08=Sol_2023.loc["2023-08-08"]
plt.plot(sol_2023_08_08.index, sol_2023_08_08["G(i)"])
plt.grid(True)
plt.xlabel("Tid")
plt.ylabel("Innstråling [W/m²]")
ax = plt.gca()

ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
