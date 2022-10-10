import numpy as np
import  serial
import matplotlib.pyplot as plt
import csv
from numpy import diff


def datataker():
 f = open("pos.txt", "w", newline="")
 writer = csv.writer(f)
 arduino = serial.Serial("COM3", 9600)
 i = 0
 while arduino.is_open:
  st = arduino.readline().decode('ascii')
  st = float(st)
  lista = [st,i]
  writer.writerow(lista)
  print(lista)
  i+=1

def grafreal(com):
 data = []
 timedata = []
 plt.figure()
 plt.ion()
 plt.show()
 plt.ylim(0,120)

 i = 0
 while True:
  st = float(com.readline().decode('ascii'))
  st= round(st)
  data.append(st)
  timedata.append(i)
  plt.pause(0.1)

  plt.cla()
  plt.plot(timedata,data)
  plt.title("Expofisica Versión 0.91")
  plt.xlabel("Tiempo(s)")
  plt.ylabel("Distancia(cm)")
  i=i+1


  print(timedata)
  print(data)


def vec(txt):
  data = np.loadtxt(txt, delimiter=',')
  y = []
  x = []
  xder=[]
  for i in range(len(data)):
   for j in range(2):
    if j == 0:
     y.append(data[i][j])
    else:
     x.append(data[i][j])

  xder = diff(y)/diff(x)
  print(xder)
  del x[-1]
  plt.plot(x,xder)
  plt.title("Grafica de velocidad VS tiempo")
  plt.xlabel("Tiempo(s)")
  plt.ylabel("Velocidad(cm/s)")
  plt.show()
  """""
  x.pop(len(x)-1)
  plt.plot(x,xder)
  plt.show()
"""


