
#bokeh serve --show excercises_slider.py
#ctrl c to quit

import numpy as np
from bokeh.io import curdoc
from bokeh.layouts import column, gridplot
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure
 
x = np.linspace(0, 2*np.pi, 200)
 
source1 = ColumnDataSource(data=dict(
    x = x,
    y = np.sin(x)
))
 
source2 = ColumnDataSource(data=dict(
    x = x,
    y = np.cos(x)
))
 
source3 = ColumnDataSource(data=dict(
    x = x,
    y = np.tan(x)
))
 
p1 = figure(plot_height = 200, plot_width = 200, title = "Sine")
p1.line('x', 
        'y', 
        source = source1, 
        line_width = 5, 
        line_alpha = 0.9)
 
p2 = figure(plot_height = 200, plot_width = 200, title = "Cosine")
p2.line('x', 
        'y', 
        source = source2, 
        line_width = 5, 
        line_alpha = 0.9)
 
p3 = figure(plot_height = 200, plot_width = 200, title = "Tangent")
p3.line('x', 
        'y', 
        source = source3, 
        line_width = 5, 
        line_alpha = 0.9)
 
freq = Slider(
    title = "Frequency", 
    value = 1.0,     
    start = 0.1, 
    end = 3.0, 
    step = 0.1)
 
freq.width = 200
 
def update_data(attrname, old, new): 
    source1.data = dict(
        x = x, 
        y = np.sin(freq.value * x) 
    )
 
    source2.data = dict(
        x = x, 
        y = np.cos(freq.value * x) 
    )
 
    source3.data = dict(
        x = x, 
        y = np.tan(freq.value * x)
    )
 
freq.on_change('value', update_data)
 
curdoc().add_root(gridplot(
    [[p1, p2], 
     [p3, None], 
     [freq, None]], 
    sizing_mode='scale_width'))
 
curdoc().title = "Sliders"

