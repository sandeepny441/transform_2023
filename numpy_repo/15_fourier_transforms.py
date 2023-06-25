import numpy as np

x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
x_fft = np.fft.fft(x)
print(x_fft)


x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
x_fft = np.fft.fft(x)
x_ifft = np.fft.ifft(x_fft)
print(x_ifft)


N = 5  # Number of points
T = 0.1  # Spacing between points
freq = np.fft.fftfreq(N, T)
print(freq)


x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
x_fft = np.fft.fft(x)
x_shifted = np.fft.fftshift(x_fft)
print(x_shifted)


x = np.mgrid[:5, :5][0]
x_fft2 = np.fft.fft2(x)
print(x_fft2)
x_ifft2 = np.fft.ifft2(x_fft2)
print(x_ifft2)



