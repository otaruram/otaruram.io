import numpy as np
import matplotlib.pyplot as plt

# Membuat Data(sin(2wt + theta))
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta): #Kalau depannya besar itu berati class
    t = np.arange(0,tAkhir, 0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

# Membuat plot
t1,y1 = sinusGenerator(1,1,4,0)
plt.plot(t1,y1)

t2,y2 = sinusGenerator(1,1,4,30)
plt.plot(t2,y2, 'b')

t3,y3 = sinusGenerator(1,1,4,60)
plt.plot(t3,y3, 'b--')

t4,y4 = sinusGenerator(1,1,4,90)
plt.plot(t4,y4, 'b-o')


# Menampilkan plot
plt.show()
    