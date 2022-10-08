import  serial
import matplotlib.pyplot as plt
import time
import os
import pandas as pd
from itertools import count

f = open("pos.txt","w")

data = []
timedata = []
i = 0
arduino = serial.Serial("COM3",9600)
archivoNombre = "pepe.csv"


def csv(com):
 i = 0
 while True:
  st = com.readline().decode('ASCII')
  #fila = (st, i)
  #writer.writerow(fila)
  f.write(st+","+str(i)+"\n")
  print(st)
  print(i)
  i+=1

def grafreal(com):
 plt.figure()
 plt.ion()
 plt.show()
 plt.ylim(0,120)
 plt.xlabel("Tiempo")
 plt.ylabel("Distancia")

 while True:
  st = float(com.readline().decode('ASCII'))
  st= round(st)
  data.append(st)
  timedata.append(i)


  plt.cla()
  plt.plot(timedata,data)
  plt.title("Expofisica Versión 0.91")
  plt.xlabel("Tiempo(s)")
  plt.ylabel("Distancia(cm)")
  plt.pause(0.1)
  i=i+1
  time.sleep(0.01)

  print(timedata)
  print(data)
def grafcsv(csv):
 df = pd.read_csv(csv)
 t = df[0]
 v = df[1]
 fig, ax = plt.subplot(figsize=(10,7))
 ax.plot(t,v)



csv(arduino)
