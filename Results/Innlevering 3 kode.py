import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime,timezone
#oppggave 1
df = pd.read_csv(
    r"C:\Users\Sande\OneDrive - Universitetet i Stavanger\Documents\GitHub\power-system-data\load\forbruk_2025.csv"
)
df["Dato"] = pd.to_datetime(df["Dato"],format="mixed",utc=True).dt.tz_convert("Europe/Oslo")


#print(df["Dato"].dtype)
#print(df.head())

#Oppgove 2
df = df.set_index("Dato")

Maaned_gjennomsnitt = df["Actual Load"].resample("MS").mean()

oversikt = Maaned_gjennomsnitt.reset_index()

oversikt.columns = ["Maaned", "Gjennomsnitt"]

oversikt["Maaned"] = oversikt["Maaned"].dt.month_name()

print(oversikt)

#Oppgove 3
oversikt.to_csv("Results/manedlig_last_2025.csv", index=False)

#oppgove 4
plt.figure(figsize=(10, 6))
plt.plot(oversikt["Maaned"], oversikt["Gjennomsnitt"], marker='o')
plt.grid(True)
plt.title("Gjennomsnittlig Månedlig Last for 2025")
plt.xlabel("Måned")
plt.ylabel("Gjennomsnittlig Last (MW)")
plt.savefig("Results/manedlig_last_2025.png")
plt.show()


#oppgave 6 : Beregn også
sortert = df.sort_values(by = "Actual Load", ascending = False)
print( "Den høyeste lasten og laveste lasten i 2025:")
Maaned_høyest=sortert.head(1)
Maaned_lavest=sortert.tail(1)
Maaned_std = df["Actual Load"].resample("MS").std()
print("Høyeste lasten i 2025:")
print(Maaned_høyest)

print("Laveste lasten i 2025:")
print(Maaned_lavest)

print("Standardavviket for hver måned i 2025:")
print(Maaned_std)

Maaned_høyest.to_csv("Results/Høyes og laveste lasten 2025 og standardavvik.csv", index=False)
Maaned_lavest.to_csv("Results/Høyes og laveste lasten 2025 og standardavvik.csv", index=False)
Maaned_std.to_csv("Results/Høyes og laveste lasten 2025 og standardavvik.csv", index=False)