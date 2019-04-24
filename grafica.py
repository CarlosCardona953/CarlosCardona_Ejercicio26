import numpy as np
import matplotlib.pyplot as plt


datos = np.loadtxt("rgk_01.dat")

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.plot(datos[:,0],datos[:,1])
plt.xlabel("x")
plt.ylabel("y")
plt.subplot(1,3,2)
plt.plot(datos[:,0],datos[:,2])
plt.xlabel("x")
plt.ylabel("y'")
plt.title("Delta x = 0.1")
plt.subplot(1,3,3)
plt.plot(datos[:,1],datos[:,2])
plt.xlabel("y")
plt.ylabel("y'")

plt.savefig("rgk_01.png")


datos = np.loadtxt("rgk_001.dat")
plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.plot(datos[:,0],datos[:,1])
plt.xlabel("x")
plt.ylabel("y")
plt.subplot(1,3,2)
plt.plot(datos[:,0],datos[:,2])
plt.xlabel("x")
plt.ylabel("y'")
plt.title("Delta x = 0.01")
plt.subplot(1,3,3)
plt.plot(datos[:,1],datos[:,2])
plt.xlabel("y")
plt.ylabel("y'")
plt.savefig("rgk_001.png")

datos = np.loadtxt("rgk_1.dat")
plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.plot(datos[:,0],datos[:,1])
plt.xlabel("x")
plt.ylabel("y")
plt.subplot(1,3,2)
plt.plot(datos[:,0],datos[:,2])
plt.xlabel("x")
plt.ylabel("y'")
plt.title("Delta x = 1")
plt.subplot(1,3,3)
plt.plot(datos[:,1],datos[:,2])
plt.xlabel("y")
plt.ylabel("y'")
plt.savefig("rgk_1.png")
