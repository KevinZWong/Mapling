import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize_scalar
import time
import json
import os
class Spline3D:
    def __init__(self, x_points=None, y_points=None, z_points=None):
        if not(x_points == None or y_points == None or z_points == None):
            self.initialize(x_points, y_points, z_points)
        # Remember to load data if there are no inputted values

    # this is done this way so I can reinitalize after load_data is run
    def initialize(self, x_points, y_points, z_points):
        self.x_values = np.array(x_points)
        self.y_values = np.array(y_points)
        self.z_values = np.array(z_points)
        self.t = np.linspace(0, 1, len(self.x_values))
        self.x_interp = CubicSpline(self.t, self.x_values)
        self.y_interp = CubicSpline(self.t, self.y_values)
        self.z_interp = CubicSpline(self.t, self.z_values)
    def plot_3d_spline(self):
        t_smooth = np.linspace(0, 1, 300)
        x_smooth = self.x_interp(t_smooth)
        y_smooth = self.y_interp(t_smooth)
        z_smooth = self.z_interp(t_smooth)
        ax = plt.axes(projection='3d')
        ax.plot3D(x_smooth, y_smooth, z_smooth)
        plt.show()

    def find_t_for_z(self, z_input):
        func_to_minimize = lambda t: (self.z_interp(t) - z_input)**2
        result = minimize_scalar(func_to_minimize, bounds=(0, 1), method='bounded')
        return result.x

    def get_x_y_for_z(self, z_input):
        t_found = self.find_t_for_z(z_input)
        x_val = self.x_interp(t_found)
        y_val = self.y_interp(t_found)
        return x_val, y_val

    def name_gen(self):
        print(time.time())
        listTime = list(str(time.time()))
        for i in range(0,len(listTime)):
            if listTime[i] == '.':
                listTime[i] = "_"
                break
        return "model_" + ''.join(listTime)
                


    def save_data(self, name=None):
        if name is None:
            name = self.name_gen()

        current_path = os.getcwd()
        path = current_path + "/mapling_models/"
        filename = f'{path}spline_data_{name}.json'

        try:
            if not os.path.exists(path):
                os.mkdir(path)
        except PermissionError:
            
            print("""PermissionError: File creation perms not granted to program")
            'mapling_models' folder missing
            To fix: create folder named 'mapling_models' or just run as administrator/sudo""")
            exit()

        # Check if the file already exists
        if os.path.exists(filename):
            user_input = input(f"The file {filename} already exists. Overwrite? (y/n): ")
            if user_input.lower() != 'y':
                print("Operation cancelled.")
                return
        

        point_data = {
            'x_values': self.x_values.tolist(), 
            'y_values': self.y_values.tolist(),
            'z_values': self.z_values.tolist()
        } 
        with open(filename, 'w') as file:
            json.dump(point_data, file)
        print(f"'/mapling_models/spline_data_{name}.json' created")
    def load_data(self, filename):

        with open(f"mapling_models/{filename}", 'r') as file:
            point_data = json.load(file)
        x_values = np.array(point_data['x_values'])
        y_values = np.array(point_data['y_values'])
        z_values = np.array(point_data['z_values'])
        self.initialize(x_values, y_values, z_values)

if __name__ == "__main__":
    path_points = [(69, 650), (155, 486), (331, 231), (426, 205), (455, 279), (418, 464), (371, 643)]
    speed_points = [1.8552631578947367, 3.3947368421052633, 5.625, 7.5, 9.375, 11.25, 13.125]


    x_points = [i[0] for i in path_points ]
    y_points = [i[1] for i in path_points ]
    x_values = np.array(x_points)
    y_values = np.array(y_points)
    z_values = np.array(speed_points)


    spline3D = Spline3D(x_points, y_points, speed_points)


    spline3D.plot_3d_spline()

    name = input("Enter a name for this modelL: ")
    spline3D.save_data(name)
    '''
    z_input = 5
    x_val, y_val = spline3D.get_x_y_for_z(z_input)
    print(f"At z = {z_input}, x = {x_val}, y = {y_val}")
    spline3D.save_data()
    '''