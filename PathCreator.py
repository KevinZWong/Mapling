
from tkinter import *
from PointSelection import PointSelectionApp
from TimeAdjustment import SliderApp
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from Spline3D import Spline3D



input("Please select points that represent path of image, line can overlap (Press enter to continue): ")
root = Tk()
app = PointSelectionApp(root)
root.mainloop()

path_points = app.getPoints()

if path_points is not None:
    print("Selected points:", path_points)
else:
    print("No points selected.")
    exit()

root = Tk()
app = SliderApp(root, 10, path_points)
root.title("Slider Widget")
root.mainloop()

speed_points = app.get_slider_values()
speed_points = speed_points


x_points = [i[0] for i in path_points ]
y_points = [i[1] for i in path_points ]
x_values = np.array(x_points)
y_values = np.array(y_points)
z_values = np.array(speed_points)



spline3D = Spline3D(x_points, y_points, speed_points)

spline3D.plot_3d_spline()

name = input("Enter a name for this modelL: ")
spline3D.save_data(name)

