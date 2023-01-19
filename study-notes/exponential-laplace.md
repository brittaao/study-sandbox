## Exponential and Laplace distribution

```python
from numpy import exp
from scipy.stats import expon

x = np.linspace(-5, 5, 1000)

fig, ax = plt.subplots()

fig.subplots_adjust(bottom=0.35)

mu_init = 0
gamma_init = 1

ax_mu = fig.add_axes([0.25, 0.1, 0.65, 0.03])
ax_gamma = fig.add_axes([0.25, 0.2, 0.65, 0.03])


def update(val):
    ax.cla()
    mu = mu_slider.val
    gamma = gamma_slider.val
    ax.set_ylim(0,10)
    ax.plot(x, (1/(2*gamma)*exp(-(abs(x-mu))/gamma)))
    fig.canvas.draw_idle()

mu_slider = Slider(
    ax = ax_mu,
    label="Mu",
    valmin=-5,
    valmax=5,
    valinit=mu_init,
    color=(0.1, 0.7, 0.0, 0.6))

gamma_slider = Slider(
    ax = ax_gamma,
    label="Gamma",
    valmin=0,
    valmax=2,
    valinit=gamma_init,
    color=(0.1, 0.7, 0.0, 0.6))

mu_slider.on_changed(update)
gamma_slider.on_changed(update)

ax.set_ylim(0,10)
ax.plot(x, (1/(2*gamma_init)*exp(-(abs(x-mu_init))/gamma_init)))
plt.show()
```
