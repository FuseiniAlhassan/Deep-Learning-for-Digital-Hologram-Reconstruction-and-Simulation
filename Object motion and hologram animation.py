# Constants
wavelength = 633e-9  # 633 nm
k = 2 * np.pi / wavelength
z = 0.01  # 1 cm propagation
dx = 10e-6
N = 128  # smaller for fast animation
# Grid setup
x = np.linspace(-N//2, N//2 - 1, N) * dx
X, Y = np.meshgrid(x, x)
# Fresnel kernel (Fourier domain)
fx = np.fft.fftfreq(N, d=dx)
FX, FY = np.meshgrid(fx, fx)
H = np.exp(-1j * np.pi * wavelength * z * (FX**2 + FY**2))

# Initialize figure and subplots
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
obj_ax, holo_ax = ax

# Empty plots
obj_im = obj_ax.imshow(np.zeros((N, N)), cmap='gray', vmin=0, vmax=1)
holo_im = holo_ax.imshow(np.zeros((N, N)), cmap='gray')
obj_ax.set_title("Moving Object")
holo_ax.set_title("Simulated Hologram")
[obj_.axis('off') for obj_ in ax]

# Bright dot object generator
def create_moving_object(frame):
    pos = int(N * (frame / num_frames))
    field = np.zeros((N, N))
    if 0 <= pos < N:
        field[N//2, pos] = 1.0
    return field

# Update function
num_frames = 50
def update(frame):
    object_field = create_moving_object(frame)
    U1 = fft2(object_field)
    U2 = U1 * H
    u2 = ifft2(U2)

    obj_im.set_data(object_field)
    holo_im.set_data(np.abs(u2)**2)

    return [obj_im, holo_im]

# Animate
ani = FuncAnimation(fig, update, frames=num_frames, interval=100, blit=True)
plt.close()
ani.save("moving_object_hologram.gif", writer='pillow', fps=10)  # Save as GIF

# Display
HTML(ani.to_jshtml())
#ANIMATE TRAINING LOSS
#Animate Training Loss
# Simulated training data
epochs = 100
loss = np.exp(-np.linspace(0, 5, epochs)) + 0.05 * np.random.randn(epochs)
loss = np.clip(loss, a_min=0, a_max=None)  # Ensure non-negative

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 5))
line, = ax.plot([], [], lw=2, color='blue')
ax.set_xlim(0, epochs)
ax.set_ylim(0, max(loss) + 0.1)
ax.set_xlabel("Epoch")
ax.set_ylabel("Loss")
ax.set_title("CNN Training Loss Over Epochs")

# Initialize function
def init():
    line.set_data([], [])
    return line,

# Update function
def update(epoch):
    x = np.arange(epoch + 1)
    y = loss[:epoch + 1]
    line.set_data(x, y)
    return line,

# Animate

ani = FuncAnimation(fig, update, frames=epochs, init_func=init, blit=True, interval=100)
plt.close()
ani.save("visualize training loss.gif", writer='pillow', fps=10)  # Save as GIF)

# Display in notebook
HTML(ani.to_jshtml())
                       