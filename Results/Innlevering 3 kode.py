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


print(df["Dato"].dtype)
print(df.head())

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
maaned_maks = df["Actual Load"].resample("MS").max()
maaned_min = df["Actual Load"].resample("MS").min()
print( "Den høyeste lasten og laveste lasten i kvar månad i 2025:")
Maaned_std = df["Actual Load"].resample("MS").std()
print("Høyeste lasten i 2025:")
print(maaned_maks)

print("Laveste lasten i 2025:")
print(maaned_min)

print("Standardavviket for hver måned i 2025:")
print(Maaned_std)

info =pd.DataFrame({
    "Maaned": oversikt["Maaned"],
    "Høyeste Last": maaned_maks.values,
    "Laveste Last": maaned_min.values,
    "Standardavvik": Maaned_std.values
})
info.to_csv("Results/Høyes og laveste lasten 2025 og standardavvik.csv", index=False)