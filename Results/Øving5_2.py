import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime,timezone

df= pd.read_csv(
    r"load\load_data.csv",parse_dates=["Time(Local)"],decimal=","
)
df["Time(Local)"] = pd.to_datetime(df["Time(Local)"], format="%d.%m.%Y %H:%M:%S %z",utc=True).dt.tz_convert("Europe/Oslo")
df = df.set_index("Time(Local)")
dags_profil=df.loc["2026-02-15"]


t = np.linspace(0, 23, 200)

L0=10000 #Grunnlast 
Ai=2000 #Amplituden til komponent i
Mui=10 #Tidspunktet for topp
sigmai=4 #Breddeparameteren til komponent

Lt=L0 +Ai*np.exp(-((t-Mui)**2/(2*sigmai**2)))
