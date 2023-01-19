---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
## Bernoulli
This is my explanation to my script.
```{code-cell} ipython3
:tags: ["hide-cell", "hide-output"]
%matplotlib widget
import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button

import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

def bernoulli(phi):
    return [phi, 1-phi]

# Define values that x can take 
x_values = ['0', '1']

# Define initial phi 
init_phi = 0.5

# Compute probabilities
probs = bernoulli(init_phi)

fig, ax = plt.subplots()

bar_container = ax.bar(x_values, probs, width=0.35, color=(0.1, 0.7, 0.0, 0.6))

fig.subplots_adjust(bottom=0.25)
axprob = fig.add_axes([0.25, 0.1, 0.65, 0.03])
prob_slider = Slider(
    ax=axprob,
    label='Probability φ',
    valmin=0.0,
    valmax=1.0,
    valinit=init_phi,
    color=(0.1, 0.7, 0.0, 0.6)
)

# Change height of bars after moving the slider
def update(val):
    probs = bernoulli(val)
    for count, rect in zip([0,1], bar_container.patches):
        rect.set_height(probs[count])
    fig.canvas.draw_idle()


# Register the update function with the slider
prob_slider.on_changed(update)

ax.set_xlim(-0.5, 1.5)
ax.set_ylim(0, 1.1)
ax.set_ylabel('Probability')
ax.set_xlabel('Value of x')
ax.set_title('Bernoulli Distribution')

plt.show()
```
