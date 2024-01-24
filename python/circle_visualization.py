import drawsvg as draw
import pandas as pd

class CircleVisualization:
    def __init__(self, methane_data, year_data):
        self.data = methane_data
        '''the data to be visualized'''

        self.years = year_data
        '''the years corresponding to the data'''

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
        # restart with a blank canvas
        self.d = draw.Drawing(self.width*self.figure_scale, self.height*self.figure_scale, origin='center', fill='black')

        # draw the background rectangle, if you want a different color
        # self.d.append(draw.Rectangle(-200,-100,400 * self.figure_scale,200 * self.figure_scale, fill='black'))

        # draw the circles
        for i, value in enumerate(self.data):
            radius = self.max_radius - self.radius_increment * i

            # increment the color
            self.increment_color(value)

            color = "rgb("+str(self.red)+","+str(self.green)+","+str(self.blue)+")"
            self.d.append(draw.Circle(self.cx, self.cy, radius, fill=color))

        # add a pale blue dot in the center ??
        # self.d.append(draw.Circle(self.cx, self.cy, 1, fill='rgb(50,50,200)'))
        return self.d
    

    def increment_color(self, value: int):
        # scale the data linearly between 0 and 255
        self.green = (value - self.min_value - 1) / self.range * 175
        # invert the green value
        self.green = 175 - self.green


    def set_circle_spacing(self, amount: int):
        self.radius_increment = amount


    def set_circle_max_size(self, amount: int):
        self.max_radius = amount

    def set_figure_scale(self, amount: int):
        self.figure_scale = amount
    