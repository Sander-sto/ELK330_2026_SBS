import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime,timezone
#oppggave 1
df = pd.read_csv(
    r"load\load_data.csv",parse_dates=["Time(Local)"],decimal=","
)
df["Time(Local)"] = pd.to_datetime(df["Time(Local)"], format="%d.%m.%Y %H:%M:%S %z",utc=True).dt.tz_convert("Europe/Oslo")

df = df.set_index("Time(Local)")
#print(df.head(5))
#print(df.index[500])
#print(df.loc["2026-01-01 03:00"])

dags_profil=df.loc["2026-02-10"]

df["Netto"] = (
    df["Production"]
    - df["Consumption"]
)

#print(df.head(5))
'''''
max_dato_df=df["Production"].idxmax()
max_df=df["Production"].max()
print("Dato",max_dato_df,"Maksimum",max_df)

min_dato_df=df["Production"].idxmin()
min_df=df["Production"].min()
print("Dato",min_dato_df,"Minimum",min_df)

gjennomsnitt_df=df["Production"].mean()
print("Gjennomsnitt",gjennomsnitt_df)


max_netto_dato_df=df["Netto"].idxmax()
max_netto_df=df["Netto"].max()

min_netto_dato_df=df["Netto"].idxmin()
min_netto_df=df["Netto"].min()

print("Maksimum netto",max_netto_df,"Dato",max_netto_dato_df)
print("Minimum netto",min_netto_df,"Dato",min_netto_dato_df)
'''''
produksjon_sum_MWh=df["Production"].sum()
produksjon_sum_TWH=produksjon_sum_MWh/1000000

print("Total produksjon i MWH",produksjon_sum_MWh,"Total produksjon i TWH",produksjon_sum_TWH)





'''''
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
'''''