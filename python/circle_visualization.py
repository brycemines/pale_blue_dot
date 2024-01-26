import drawsvg as draw
import pandas as pd

class CircleVisualization:
    def __init__(self, methane_data):
        '''Initialize the class with the data to be visualized'''

        self.data = methane_data
        '''the data to be visualized'''

        self.max_value = max(methane_data)
        '''the maximum value in the data'''

        self.min_value = min(methane_data)
        '''the minimum value in the data'''

        self.range = max(methane_data) - min(methane_data)
        '''the range of the data'''

        self.width = 200
        '''width of the drawing'''

        self.height = 100
        '''height of the drawing'''

        self.d = draw.Drawing(self.width, self.height, origin='center', fill='black')
        '''blank drawing'''

        self.green = 0
        '''green value for the circles'''

        self.red = 200
        '''red value for the circles'''

        self.blue = 50
        '''blue value for the circles'''

        self.radius_increment = 10
        '''amount to increment the radius of each circle'''

        self.max_radius = 100
        '''the maximum radius of the largest circle'''

        self.cx = 0
        '''x coordinate of the center of the circle'''

        self.cy = 50
        '''y coordinate of the center of the circle'''

        self.figure_scale = 1
        '''scales the size of the figure'''


    def draw(self):
        '''Draw the overlapping concentric circles'''
        # restart with a blank canvas
        self.d = draw.Drawing(self.width*self.figure_scale, self.height*self.figure_scale, origin='center', fill='black')

        # draw the circles
        for i, value in enumerate(self.data):
            radius = self.max_radius - self.radius_increment * i

            # increment the color
            self.increment_color(value)

            # draw the circle
            color = "rgb("+str(self.red)+","+str(self.green)+","+str(self.blue)+")"
            self.d.append(draw.Circle(self.cx, self.cy, radius, fill=color))

        return self.d


    def draw_colorbar(self):
        '''Draw the colorbar'''
        # restart with a blank canvas
        self.d = draw.Drawing(self.width*self.figure_scale, self.height*self.figure_scale, origin='center', fill='black')

        # find the "max color". 
        self.increment_color(self.max_value)
        color_min = "rgb("+str(self.red)+","+str(self.green)+","+str(self.blue)+")"

        # find the "min color"
        self.increment_color(self.min_value)
        color_max = "rgb("+str(self.red)+","+str(self.green)+","+str(self.blue)+")"

        gradient = draw.LinearGradient(250, -50, 275, 50)
        gradient.add_stop(0, color_max, 1)
        gradient.add_stop(1, color_min, 1)
        self.d.append(draw.Rectangle(275,-50,25,100, stroke='black', stroke_width=0.002, fill=gradient))
        return self.d

    
    def increment_color(self, value: int):
        '''scale the data linearly between 0 and 175, keeping relative spacing'''
        self.green = (value - self.min_value) / self.range * 175


    def set_circle_spacing(self, amount: int):
        '''set the amount to increment the radius of each circle'''
        self.radius_increment = amount


    def set_circle_max_size(self, amount: int):
        '''set the maximum radius of the largest circle'''
        self.max_radius = amount

    def set_figure_scale(self, amount: int):
        '''scale the size of the figure'''
        self.figure_scale = amount
    