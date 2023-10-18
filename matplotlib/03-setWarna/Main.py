import numpy as np
import matplotlib.pyplot as plt

# membuat data
# membuat plot
# menampilkan plot

def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
 t = np.arange(0, tAkhir, 0,1)
 y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
 return t,y

t1,y1 = sinusGenerator(1,1,4,0)
t2,y2 = sinusGenerator(1,1,4,90)
t3,y3 = sinusGenerator(1,1,4,180)

plt.plot(t1,y1)
plt.plot(t2,y2)
plt.plot(y3,y3)

plt.savefig('plot.png')