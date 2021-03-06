import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mplanimations as ans

s = .25

x = np.linspace(-20, 20, 500)

def f(sigma):
    return (1/(sigma*np.sqrt(2*np.pi)))*np.exp((-(x**2))/(2*(sigma**2)))

def g(sigma):
    return np.exp(-((sigma**2)*(x**2))/2)-1.5

fig, ax = plt.subplots()

p1 = ax.plot(x, f(s), c='black')[0]
p2 = ax.plot(x, g(s), c='black')[0]

ax.text(-20, .5, r'$f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{\frac{-x^2}{2\sigma^2}}$', size=15)
ax.text(-20, -1, r'$\int_{-\infty}^{\infty}f(x)e^{-ikx}dx$', size=15)

ax.axes.get_yaxis().set_visible(False)
ax.set_xlabel('Wavelength/Wavenumber')
sigmatext = ax.text(10, .5, r'$\sigma = .25$', size=15)

ts = [ans.Transitions() for i in range(5)]

def animate(i):
    ts[0].var_transition(i, 1, .25, 2, p1, f)
    ts[1].var_transition(i, 1, .25, 2, p2, g)
    ts[2].var_transition(i, 3, 2, .25, p1, f)
    ts[3].var_transition(i, 3, 2, .25, p2, g)
    if i <= 100 or i >= 200:
        sigmatext.set_text(r'$\sigma = $' + str(round(ts[0].var, 2)))
    else:
        sigmatext.set_text(r'$\sigma = $' + str(round(ts[2].var, 2)))
    

ani = animation.FuncAnimation(fig, animate, interval=20, frames=250, repeat=False)

plt.show()
