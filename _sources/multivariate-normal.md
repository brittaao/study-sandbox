## Multivariate normal distribution
This is my explanation to my script.
```python
%matplotlib widget
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.widgets import Slider, Button
import numpy as np
from scipy.stats import multivariate_normal 

matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(8, 10))
fig.subplots_adjust(bottom=0.35)

ax_x_slider = fig.add_axes([0.25, 0.1, 0.65, 0.03])
ax_y_slider = fig.add_axes([0.25, 0.2, 0.65, 0.03])
ax_corr_slider = fig.add_axes([0.25, 0.3, 0.65, 0.03])

x_mean, y_mean = 0, 0
variance_x, variance_y, correlation_xy = 2, 2, 0

x_slider = Slider(
    ax = ax_x_slider,
    label="μ of X",
    valmin=-5,
    valmax=5,
    valinit=x_mean,
    valstep = np.arange(-5, 5, 0.5),
    color=(0.1, 0.7, 0.0, 0.6))

y_slider = Slider(
    ax= ax_y_slider,
    label="μ of Y",
    valmin=-5,
    valmax=5,
    valinit= y_mean,
    valstep = np.arange(-5, 5, 0.5),
    color=(0.1, 0.7, 0.0, 0.6))

corr_slider = Slider(
    ax = ax_corr_slider,
    label= "Correlation X, Y",
    valmin=-1,
    valmax=1,
    valinit= 0,
    valstep = np.arange(-1, 1, 0.1),
    color=(1.0, 0.7, 0.0, 0.6))

# Change height of bars after moving the slider
def update_x_mean(val):
    ax.cla()
    global x_mean
    x_mean = val
    dist = update_normal_distribution()
    surf = ax.plot_surface(x, y, dist.pdf(pos), cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)    
    fig.canvas.draw_idle()
    
def update_y_mean(val):
    ax.cla()
    global y_mean
    y_mean = val
    dist = update_normal_distribution()
    surf = ax.plot_surface(x, y, dist.pdf(pos), cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)    
    fig.canvas.draw_idle()
    
def update_correlation(val):
    ax.cla()
    global correlation_xy
    correlation_xy = val
    dist = update_normal_distribution()
    surf = ax.plot_surface(x, y, dist.pdf(pos), cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)    
    fig.canvas.draw_idle()
    
def update_normal_distribution():
    global x_mean, y_mean, variance_x, variance_y, correlation_xy, covariance
    covariance = correlation_xy*np.sqrt(variance_x)*np.sqrt(variance_y)
    rv = multivariate_normal(
        [x_mean, y_mean], 
        [[variance_x, covariance], [covariance, variance_y]], 
        allow_singular=True)
    return rv

# Register the update function with each slider
x_slider.on_changed(update_x_mean)
y_slider.on_changed(update_y_mean)
corr_slider.on_changed(update_correlation)



x, y = np.mgrid[-5:5:.005, -5:5:.005]
pos = np.dstack((x, y))
dist = update_normal_distribution()

surf = ax.plot_surface(x, y, dist.pdf(pos), cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

plt.show()
```
This is some more explanation.
