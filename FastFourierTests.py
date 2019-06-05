import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import tensorflow as tf

# plotting X/Y, 3 sine waves
samples = 1000 # 1000 samples, assume 100Hz max
x = np.arange(0,1,(1/samples)) # 0 - 0.5 seconds, 0.005 step
f1 = 2 * np.sin(2*np.pi*x*2) # 2 Hz signal @ 2V
f2 = 0.2 * np.sin(2*np.pi*x*20) # 10 Hz signal @ 0.2V
f3 = 0.1 * np.sin(2*np.pi*x*100) # 100 Hz signal @ 0.5V peak
f4 = 0.5 * np.sin(2*np.pi*x*400) # 100 Hz signal @ 0.5V peak
signal = np.add(np.add(np.add(f1,f2),f3), f4)
plt.xlabel('time(s)')
plt.ylabel('voltage(V)')
plt.plot(x,signal)
plt.show()

# Fourier transform
freq = np.fft.fftfreq(x.shape[-1])
freq = freq * samples * -1     # normalise
print(x.shape[-1])
spectrum = np.fft.fft(signal)
spectrum = spectrum/samples     #normalise
plt.xlabel('freq(Hz)')
plt.ylabel('voltage(V)')
axes = plt.gca()
axes.set_xlim([0,500])
xRange = np.arange(0,500,40) 
plt.xticks(xRange)
plt.plot(freq, spectrum.real, freq, spectrum.imag)
plt.show()

# inverse fourier transform
s = np.fft.ifft(spectrum)
plt.xlabel('time(s)')
plt.ylabel('voltage(V)')
plt.plot(x, s.real, 'b-', x, s.imag, 'r--') # plot two values against the same x
plt.show()

# plotting XY/TZ
c1 = np.arange(0,10,1)
c2 = np.arange(1,11,1)
t = np.arange(1,10,1)
t2 = np.arange(1,10,1)
plt.plot(t,c1,t2,c2)
plt.show()

# curve fitting
# classifier, not image based
# convolution