import  serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import  threading
import  numpy as np
import time

data = []
timedata = []
i = 0
#file = open('lucasescaga.csv')
arduino = serial.Serial("COM3",9600)
plt.figure()
plt.ion()
plt.show()
plt.ylim(0,120)
plt.xlabel("Tiempo")
plt.ylabel("Distancia")



while True:
  st = float(arduino.readline().decode('ASCII'))
  st= round(st)
  data.append(st)
  timedata.append(i)
  """""
  if len(data) >200:
         data.pop(0)
  if len(timedata)>200:
      timedata.pop(0)
  """""


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