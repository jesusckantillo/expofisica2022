import  matplotlib.pyplot as plt
import numpy as  np
from matplotlib.figure import Figure


def grafpos(txt):
 data = np.loadtxt(txt,delimiter=',')
 y =[]
 x=[]
 for i in range(len(data)):
  for j in range(2):
   if j ==0:
    y.append(data[i][j])
   else:
    x.append(data[i][j])

 plt.title("Grafica de posición contra tiempo")
 plt.xlabel("Tiempo(s)")
 plt.ylabel("Distancia(cm)")
 plt.plot(x,y)
 plt.show()


"""""
 fig, axs = plt.subplots(1,1,dpi=80,figsize=(15,15))
 axs[0].plot(x,y,color='m')
 return fig
"""""


