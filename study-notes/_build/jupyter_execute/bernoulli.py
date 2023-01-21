#!/usr/bin/env python
# coding: utf-8

# # Bernoulli
# The Bernoulli distribution is probably one of the first distributions to come across. It is a special case
# of the binomial distribution with n = 1 (where n is the number of trials conducted). If X is a random variable
# that takes value 1 with probability p and 0 with probability q, then it holds: 
# 
# $$
# Pr(X=1) = p = 1 - Pr(X=0) = 1 - q
# $$
# 
# ```{note}
# The output in this jupyter book will unfortunately not be interactive. This is because the widgets require 
# a running python kernel, but jupyter books renders markdown and .ipynb files into html (so no Python 
# kernel running).
# ```

# In[1]:


get_ipython().run_line_magic('matplotlib', 'widget')
import ipywidgets as widgets
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np

default_color = "#81b69d80"


# The code for the plot: 
# ```
# def bernoulli(p):
#     '''Return probabilities p and q'''
#     return [p, 1-p]
# 
# # Define values that x can take 
# x_values = ['0', '1']
# 
# # Define initial p 
# init_p = 0.5
# 
# # Compute probabilities
# probs = bernoulli(init_p)
# 
# # Set up bar plot
# fig, ax = plt.subplots()
# 
# bar_container = ax.bar(x_values, probs, width=0.35, color=default_color)
# 
# fig.subplots_adjust(bottom=0.25)
# axprob = fig.add_axes([0.25, 0.1, 0.65, 0.03])
# prob_slider = Slider(
#     ax=axprob,
#     label='Probability p',
#     valmin=0.0,
#     valmax=1.0,
#     valinit=init_p,
#     color=default_color
# )
# 
# # Change height of bars after moving the slider
# def update(val):
#     probs = bernoulli(val)
#     for count, rect in zip([0,1], bar_container.patches):
#         rect.set_height(probs[count])
#     fig.canvas.draw_idle()
# 
# 
# # Register the update function with the slider
# prob_slider.on_changed(update)
# 
# ax.set_xlim(-0.5, 1.5)
# ax.set_ylim(0, 1.1)
# ax.set_ylabel('Probability P(X)')
# ax.set_xlabel('Value of X')
# ax.set_title('Bernoulli Distribution')
# 
# plt.show()
# ```
# 
# ![bernoulli](./_static/bernoulli.gif)
