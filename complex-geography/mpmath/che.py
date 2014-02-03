#!/usr/bin/python

from matplotlib import *
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from mpl_toolkits.axes_grid.axislines import Subplot
import mpl_toolkits.axisartist as AA
from matplotlib.figure import Figure
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.axislines import Subplot

fig = plt.figure(1, (3,3))

ax = Subplot(fig, 111)
fig.add_subplot(ax)

ax.axis['right'].set_visible(False)
ax.axis['top'].set_visible(False)

canvas.print_figure('che.svg',dpi=500)
