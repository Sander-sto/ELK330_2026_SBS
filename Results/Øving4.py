import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime,timezone
#oppggave 1
df = pd.read_csv(
    r"C:\Users\Sande\OneDrive - Universitetet i Stavanger\Documents\GitHub\power-system-data\load\load_data.csv",parse_dates=["Time(Local)"],decimal=","
)
df["Time(Local)"] = pd.to_datetime(df["Time(Local)"], format="%d.%m.%Y %H:%M:%S %z",utc=True).dt.tz_convert("Europe/Oslo")

df = df.set_index("Time(Local)")
#print(df.head(5))
#print(df.index[500])
#print(df.loc["2026-01-01 03:00"])

dags_profil=df.loc["2026-02-10"]

dags_profil.plot(
    y=["Consumption"],
    figsize=(10, 5)
)

plt.title("Forbruk")
plt.xlabel("Tid")
plt.ylabel("Effekt [MW]")
plt.grid(True)
plt.legend()

plt.show()