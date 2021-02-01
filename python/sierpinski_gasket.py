
from pylab import *
import numpy as np


def midpoint(point1, point2):
    point1_x, point1_y = point1
    point2_x, point2_y = point2
    mid_pt = (point1_x+point2_x)/2, (point1_y+point2_y)/2
    print(f"Midpoint of ({point1}),({point2}) is ({mid_pt})")
    return mid_pt


def plot(x, y, color):
    scatter(x, y, s=50, marker='o', color=[color])


def roll_dice():
    from random import randrange
    dice_roll = randrange(1, 7)
    return dice_roll


def main():
    x = [0, -10, 10]
    y = [10, 0, 0]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_yticks(np.arange(min(y), max(y)+1, 1.0)) 
    ax.set_xticks(np.arange(min(x), max(x)+1, 1.0)) 
    plot(x, y, '#000000')
    triplot(x,y, color='#000000')

    midpoint_x = 3
    midpoint_y = 3
    plot([midpoint_x], [midpoint_y], '#FF0000')

    iteration = 0
    while iteration <= 1:
        dice = roll_dice()
        print(f"Iteration :{iteration} ; Dice:{dice}")
        if (dice <= 2):
            midpoint_x, midpoint_y = midpoint(
                [midpoint_x, midpoint_y], [x[0], y[0]])
        if (dice <= 4 and dice > 2):
            midpoint_x, midpoint_y = midpoint(
                [midpoint_x, midpoint_y], [x[1], y[1]])
        if (dice <= 6 and dice > 4):
            midpoint_x, midpoint_y = midpoint(
                [midpoint_x, midpoint_y], [x[2], y[2]])

        plot([midpoint_x], [midpoint_y], '#FF0000')
        iteration += 1
    grid()
    show()


main()
