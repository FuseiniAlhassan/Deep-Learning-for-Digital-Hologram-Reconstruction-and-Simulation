wavelength = 633e-9
k = 2 * np.pi / wavelength
z = 0.01
dx = 10e-6
N = 512
x = np.linspace(-N//2, N//2 - 1, N) * dx
X, Y = np.meshgrid(x, x)
radius = 50e-6
object_field = np.exp(-((X**2 + Y**2)/ (radius**2)))
plt.figure(figsize=(5,5))
plt.title("Object field amplitude")
plt.imshow(object_field, cmap='gray')
plt.colorbar
plt.axis('off')
plt.savefig("object field")
plt.show()
#fresnel propagation using transfer function approach
fx = np.fft.fftfreq(N, d=dx)
FX, FY = np.meshgrid(fx, fx)
H = np.exp(-1j * np.pi * wavelength * z * (FX**2 + FY**2))  # Fresnel kernel
U1 = fft2(object_field)
U2 = U1 * H
u2 = ifft2(U2)
#plot propagated field and amplitude phase
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.title("Amplitude at Hologram Plane")
plt.imshow(np.abs(u2), cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Phase at Hologram Plane")
plt.imshow(np.angle(u2), cmap='twilight')
plt.axis('off')

plt.tight_layout()
plt.savefig("Amplitude and Phsde at hologram plane")
plt.show()