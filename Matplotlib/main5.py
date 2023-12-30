import matplotlib.pyplot as plt
import numpy as np

# membuat data
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta): #Kalau depannya besar itu berati class
    t = np.arange(0,tAkhir, 0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

amplitudo = 1
frekuensi = 1
theta = 0
tAkhir = 4

t,y = sinusGenerator(amplitudo,frekuensi,tAkhir,theta)

# membuat plot

judul = 'Anjing\n'
rumus = r'$ \mathcal{Y} = A.sin(2 \omega t + \theta)$'
parameter1 = r'$ A = $' + str(amplitudo) + 'cm'
parameter2 = r'$\omega = $' + str(frekuensi) + r'$\mathit{Hz}$' +','
parameter3 = r'$ \theta = $' + str(theta) + r'$ ^{0} $'
plt.plot( t,y )

plt.title( judul + rumus + parameter1 + parameter2 )

plt.xlabel('waktu(detik)')
plt.ylabel ('magnituda(cm)')

# Show

plt.show()