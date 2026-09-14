import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime,timezone


df= pd.read_csv(
    r"load\productionconsumption-2022.csv",decimal=","
)
df["Time(Local)"] = pd.to_datetime(df["Time(Local)"], format="%d.%m.%Y %H:%M:%S %z",utc=True).dt.tz_convert("Europe/Oslo")
df = df.set_index("Time(Local)")
df["Consumption"] = pd.to_numeric(
    df["Consumption"].str.replace(",", "."),
    errors="coerce"
)
dags_profil_2022=df.loc["2022-02-17"]


t = np.linspace(0, 23, 200)

L0=16000 #Grunnlast 
#Første komponent
A1=3750 #Amplituden til komponent i
Mu1=9 #Tidspunktet for topp
sigma1=3 #Breddeparameteren til komponent

#Andre komponent
A2=3200 #Amplituden til komponent i
Mu2=18 #Tidspunktet for topp
sigma2=3 #Breddeparameteren til komponent

#tredhe komponent
A3=750 #Amplituden til komponent i
mu3=0 #Tidspunktet for topp
sigma3=1 #Breddeparameteren til komponent

Lt=L0 +A1*np.exp(-((t-Mu1)**2/(2*sigma1**2)))+A2*np.exp(-((t-Mu2)**2/(2*sigma2**2)))+A3*np.exp(-((t-mu3)**2/(2*sigma3**2)))

plt.plot(
    dags_profil_2022.index.hour,
    dags_profil_2022["Consumption"],
    label="Målt forbruk"
)

plt.plot(
    t,
    Lt,
    label="Modell"
)

plt.xlabel("Tid [h]")
plt.ylabel("Last")
plt.title("Dagsprofil 17.02.2022")
plt.grid()
plt.legend()

plt.show()