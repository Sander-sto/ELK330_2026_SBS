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


t = np.linspace(0, 23, 24)

L0=17000 #Grunnlast 
#Første komponent morgen
A1=3000 #Amplituden til komponent i
Mu1=8 #Tidspunktet for topp
sigma1=3 #Breddeparameteren til komponent
Morgen_plott=L0 +A1*np.exp(-((t-Mu1)**2/(2*sigma1**2)))

#Andre komponent kveld
A2=2200 #Amplituden til komponent i
Mu2=18 #Tidspunktet for topp
sigma2=3 #Breddeparameteren til komponent
Kveld_plott =L0 +A2*np.exp(-((t-Mu2)**2/(2*sigma2**2)))
#tredhe komponent natt

A3=-1700 #Amplituden til komponent i
mu3=4 #Tidspunktet for topp
sigma3=2 #Breddeparameteren til komponent
Natt_plott =L0 +A3*np.exp(-((t-mu3)**2/(2*sigma3**2)))

Lt=L0 +A1*np.exp(-((t-Mu1)**2/(2*sigma1**2)))+A2*np.exp(-((t-Mu2)**2/(2*sigma2**2)))+A3*np.exp(-((t-mu3)**2/(2*sigma3**2)))

plt.plot(
    dags_profil_2022.index.hour,
    dags_profil_2022["Consumption"],
    label="Målt forbruk",
    marker="o",
)
plt.xlabel("Tid [T]")
plt.xticks(np.arange(0, 24, 1))
plt.ylabel("Last")
plt.title("Dagsprofil 17.02.2022 - observerte data")
plt.grid()
plt.legend()


plt.show()

plt.plot(
    t,Lt,
    label="Modell",marker="o",color="orange")

plt.xlabel("Tid [T]")
plt.xticks(np.arange(0, 24, 1))
plt.ylabel("Last")
plt.title("Dagsprofil 17.02.2022 - Modell kurve")
plt.grid()
plt.legend()
plt.show()




#Plott av begge kurvene
plt.plot(
    dags_profil_2022.index.hour,
    dags_profil_2022["Consumption"],
    label="Målt forbruk",
    marker="o",
)


plt.plot(
    t,
    Lt,
    label="Modell",
    marker="o"
)
plt.plot(
    t, Morgen_plott,linestyle="--",label="Morgenkomponent"
)
plt.plot(
    t, Kveld_plott,linestyle="--",label="Kveldskomponent"
)
plt.plot(
    t, Natt_plott,linestyle="--",label="Nattkomponent"
)

plt.xlabel("Tid [T]")
plt.xticks(np.arange(0, 24, 1))
plt.ylabel("Last")
plt.title("Dagsprofil 17.02.2022 Modell og observerte data")
plt.grid()
plt.legend()


plt.show()