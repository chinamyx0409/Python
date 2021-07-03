#C:\Users\admin\db2\datasets\Datasets\Data Visualization Lab6 20210628 interactive.py
#bokeh serve --show Data Visualization 'Lab6 20210628 interactive.py'
#ctrl c to quit

#Data Visualization Lab6 20210628 interactive.py
import math
from bokeh.transform import cumsum
from bokeh.plotting import figure, output_file, show
from bokeh.io import curdoc
from bokeh.layouts import row, column, gridplot
from bokeh.models import ColumnDataSource
import pandas as pd
from bokeh.palettes import Spectral

df = pd.DataFrame(dict(    
    x=['Apple','Orange','Durian','Pear','Pineapple'],
    y=[2, 4, 6, 8.5, 10]
))

df['colors'] = Spectral[len(df.x)]
source = ColumnDataSource(df)
df['angles'] = df['y'] / df['y'].sum() * 2*math.pi

p1 = figure(x_range=source.data['x'], 
            plot_width=400, 
            plot_height=400, 
            tools='tap,pan,wheel_zoom,box_zoom,reset')
p1.vbar(x = "x", 
       width = 0.5, 
       bottom = 0,
       top = "y", 
       color = 'colors',
       source=source)  


p2 = figure(y_range=source.data['x'], 
            plot_width=400, 
            plot_height=400, 
            tools='tap,pan,wheel_zoom,box_zoom,reset')
p2.hbar(y = "x", 
       height = 0.5, 
       left = 0,
       right = "y", 
       color = 'colors',
       source=source)  


p3 = figure(plot_width=400, 
            plot_height=400, 
            tools='tap,pan,wheel_zoom,box_zoom,reset')

p3.wedge(x=0,
         y=1, 
         radius=0.7,
         start_angle=cumsum('angles', include_zero=True), 
         end_angle=cumsum('angles'),
         line_color="white",         
         fill_color='colors', 
         legend_field='x', 
         source=source)       
p3.axis.visible = False


def hbar_select(attrname, old, new):
    print("Selected column(s):", new)
    print("Selected column(s):", source.selected.indices)
    
source.selected.on_change('indices',hbar_select)
    
curdoc().add_root(row(p1,p2,p3, width = 700))
curdoc().title = "Interactive Graph"