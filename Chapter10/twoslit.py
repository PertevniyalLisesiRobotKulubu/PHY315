# Author: Richard Fitzpatrick
# Modified from  http://matplotlib.org/examples/widgets/slider_demo.py
# Requires numpy and matplotlib

"""
Widget to illustrate two-slit, far-field interference
due to monochromatic light source of negligble angular extent.
Plots intensity of light versus angle as function
of d/lambda and theta_0, where d is slit-spacing,
lambda is wavelength, and theta_0 is angle of
incidence. 
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Generate initial plot
t   = np.arange(-0.5,0.5,0.001)
t00 = 0.
d0  = 5.
x   = np.pi*d0*(np.sin(t*np.pi) - np.sin(t00*np.pi))
I   = np.cos(x)*np.cos(x)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.20, bottom=0.30)
l,  = plt.plot(t, I, lw=2, color='red')
l1, = plt.plot([t00,t00], [0.,1.1], lw=2, color='blue', ls='dotted')
plt.axis([-0.5, 0.5, 0., 1.1])
plt.xlabel(r'$\theta/\pi$', size='large')
plt.ylabel('$I$', size='large')

# Generate slider
axcolor = 'lightgoldenrodyellow'
axd     = plt.axes([0.20, 0.15, 0.65, 0.03], axisbg=axcolor)
axt     = plt.axes([0.20, 0.10, 0.65, 0.03], axisbg=axcolor)
sd      = Slider(axd, r'$d/\lambda$', 0., 10., valinit=d0)
st0     = Slider(axt, r'$\theta_0/\pi$', -0.5, 0.5, valinit=t00)

# Update plot using slider data
def update(val):
    d  = sd.val
    t0 = st0.val
    x  = np.pi*d*(np.sin(t*np.pi) - np.sin(t0*np.pi))
    l.set_ydata(np.cos(x)*np.cos(x))
    l1.set_xdata([t0,t0])
    fig.canvas.draw_idle()
sd.on_changed(update)
st0.on_changed(update)

# Generate reset button
resetax = plt.axes([0.8, 0.02, 0.1, 0.04])
button  = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sd.reset()
    st0.reset()
button.on_clicked(reset)

plt.show()
