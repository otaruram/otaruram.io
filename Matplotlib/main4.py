import matplotlib.pyplot as plt
import numpy as np



# Membuat data
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta): #Kalau depannya besar itu berati class
    t = np.arange(0,tAkhir, 0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

t,y = sinusGenerator(1,1,4,0)


# membuat plot
plt.plot(t,y)

#   settings axis nilai max and minim
plt.axis([0,4,-3,3])

# Show
plt.show()