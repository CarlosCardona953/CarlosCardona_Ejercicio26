import numpy as np
import matplotlib.pyplot as plt

#Runge Kutta

datos = np.loadtxt("rgk.dat")

plt.figure(figsize=(15,15))

plt.subplot(3,3,2)
plt.plot(datos[:,0],datos[:,1])
plt.xlabel("tiempo")

plt.title("Ruge Kutta")
plt.xlim(0,12)
plt.ylim(-1.5,1.5)
plt.subplot(3,3,5)
plt.plot(datos[:,0],datos[:,2])
plt.xlabel("tiempo")

plt.xlim(0,12)
plt.ylim(-1.5,1.5)

plt.subplot(3,3,8)
plt.plot(datos[:,1],datos[:,2])
plt.xlabel("Posicion")

plt.xlim(-2,2)
plt.ylim(-2,2)

#Leapfrog

datos1 = np.loadtxt("leapfrog.dat")


plt.subplot(3,3,3)
plt.plot(datos1[:,0],datos1[:,1])
plt.xlabel("tiempo")

plt.title("Leapfrog")
plt.xlim(0,12)
plt.ylim(-1.5,1.5)
plt.subplot(3,3,6)
plt.plot(datos1[:,0],datos1[:,2])
plt.xlabel("tiempo")

plt.xlim(0,12)
plt.ylim(-1.5,1.5)

plt.subplot(3,3,9)
plt.plot(datos1[:,1],datos1[:,2])
plt.xlabel("Posicion")

plt.xlim(-2,2)
plt.ylim(-2,2)


#Euler
datos2 = np.loadtxt("euler.dat")

plt.subplot(3,3,1)
plt.plot(datos2[:,0],datos2[:,1])
plt.xlabel("tiempo")
plt.ylabel("Posicion")
plt.title("Euler")
plt.xlim(0,12)
plt.ylim(-1.5,1.5)
plt.subplot(3,3,4)
plt.plot(datos2[:,0],datos2[:,2])
plt.xlabel("tiempo")
plt.ylabel("Velocidad")
plt.xlim(0,12)
plt.ylim(-1.5,1.5)

plt.subplot(3,3,7)
plt.plot(datos2[:,1],datos2[:,2])
plt.xlabel("Posicion")
plt.ylabel("Velocidad")
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.savefig("solucion.png")

