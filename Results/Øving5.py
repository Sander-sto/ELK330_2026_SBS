#Oppgave 1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime,timezone

t = np.linspace(0, 23, 200)

L0=10000 #Grunnlast 
Ai=2000 #Amplituden til komponent i
Mui=10 #Tidspunktet for topp
sigmai=4 #Breddeparameteren til komponent

Lt=L0 +Ai*np.exp(-((t-Mui)**2/(2*sigmai**2)))

plt.plot(t,Lt)
plt.title("Lastprofil")
plt.xlabel("Tid [h]")
plt.ylabel("Last [kW]")
plt.grid(True)
plt.show()
plt.legend(["Lastprofil"])
