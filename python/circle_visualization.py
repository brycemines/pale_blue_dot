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

        self.red = 255
        '''red value for the circles'''

        self.blue = 64
        '''blue value for the circles'''

        self.radius_increment = 10
        '''amount to increment the radius of each circle'''

        self.max_radius = 100
        '''the maximum radius of the largest circle'''

        self.cx = 0
        '''x coordinate of the center of the circle'''

        self.cy = 50
        '''y coordinate of the center of the circle'''


    def draw(self):
        # restart with a blank canvas
        self.d = draw.Drawing(self.width, self.height, origin='center', fill='black')

        # draw the background rectangle
        self.d.append(draw.Rectangle(-200,-100,400,200, fill='black'))

        # draw the circles
        for i, value in enumerate(self.data):
            radius = self.max_radius - self.radius_increment * i

            # increment the color
            self.increment_color(value)

            color = "rgb("+str(self.red)+","+str(self.green)+","+str(self.blue)+")"
            self.d.append(draw.Circle(self.cx, self.cy, radius, fill=color))

            # draw the year label at the radius + center y
            print(self.years[i])
            self.d.append(draw.Text(str(self.years[i]), x=self.cx, y=radius + self.cy + 20, font_size=5, fill='white'))
        return self.d
    

    def increment_color(self, value: int):
        # scale the data between 0 and 255
        self.green = (((value / self.max_value)**16) * 255)


    def set_circle_spacing(self, amount: int):
        self.radius_increment = amount


    def set_circle_max_size(self, amount: int):
        self.max_radius = amount
    


if __name__ == "__main__":
    methane_data = pd.read_csv('../data/methane.csv')

    year_values = methane_data['TIME'].values
    methane_values = methane_data['unknown'].values

    # get the most recent 10 years
    recent_methane_values = methane_values[-10:]
    recent_year_values = year_values[-10:]

    inv_methane_values = recent_methane_values[::-1]
    inv_year_values = recent_year_values[::-1]

    methane_viz = CircleVisualization(inv_methane_values, inv_year_values)
    methane_viz.draw().save_svg('methane.svg')
