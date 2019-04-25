import numpy as np
import matplotlib.pyplot as plt

#Runge Kutta

datos = np.loadtxt("rgk_01.dat")

plt.figure(figsize=(15,15))

plt.subplot(3,3,2)
plt.plot(datos[:,0],datos[:,1])
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(0,12)
plt.ylim(-1.5,1.5)
plt.subplot(3,3,5)
plt.plot(datos[:,0],datos[:,2])
plt.xlabel("x")
plt.ylabel("y'")
plt.xlim(0,12)
plt.ylim(-1.5,1.5)
plt.title("Delta x = 0.1")
plt.subplot(3,3,8)
plt.plot(datos[:,1],datos[:,2])
plt.xlabel("y")
plt.ylabel("y'")
plt.xlim(-2,2)
plt.ylim(-2,2)


#datos = np.loadtxt("leapfrog.dat")
#plt.figure(figsize=(15,5))

#plt.subplot(1,3,1)
#plt.plot(datos[:,0],datos[:,1])
#plt.xlabel("x")
#plt.ylabel("y")
#plt.subplot(1,3,2)
#plt.plot(datos[:,0],datos[:,2])
#plt.xlabel("x")
#plt.ylabel("y'")
#plt.title("Delta x = 0.01")
#plt.subplot(1,3,3)
#plt.plot(datos[:,1],datos[:,2])
#plt.xlabel("y")
#plt.ylabel("y'")
#plt.savefig("rgk_001.png")

#Euler
datos2 = np.loadtxt("euler.dat")

plt.subplot(3,3,1)
plt.plot(datos2[:,0],datos2[:,1])
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(0,12)
plt.ylim(-1.5,1.5)
plt.subplot(3,3,4)
plt.plot(datos2[:,0],datos2[:,2])
plt.xlabel("x")
plt.ylabel("y'")
plt.xlim(0,12)
plt.ylim(-1.5,1.5)
plt.title("Delta x = 1")
plt.subplot(3,3,7)
plt.plot(datos2[:,1],datos2[:,2])
plt.xlabel("y")
plt.ylabel("y'")
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.savefig("rgk_1.png")

