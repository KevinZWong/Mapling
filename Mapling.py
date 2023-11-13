
import tkinter as tk
from pointSelection import PointSelectionApp
from createGraph import AppliedMath



def main():
  
    input("Please select points that represent path of image, line can overlap (Press enter to continue): ")
    root = tk.Tk()
    app = PointSelectionApp(root)
    root.mainloop()

    path_points = app.getPoints()
    if path_points is not None:
        print("Selected points:", path_points)
    else:
        print("No points selected.")
        exit()


    input("Please select points that represent speed of image across path (Press enter to continue): ")
    
    root = tk.Tk()
    app = PointSelectionApp(root, "Time", "Speed")
    root.mainloop()
    speed_points = app.getPoints()
    if speed_points is not None:
        print("Selected points:", speed_points)
    else:
        print("No points selected.")
        exit()
    '''
    ######## test ########

    path_points = [(69, 650), (155, 486), (331, 231), (426, 205), (455, 279), (418, 464), (371, 643)]
    speed_points = [(26, 660), (132, 459), (251, 275), (404, 238), (443, 349), (444, 443), (462, 637)]
    ######################
    '''
    
    
   
   
    path_calc = AppliedMath(path_points) 
    path_graph = path_calc.create_graph() 
    print(path_graph["coefficients"])
    
    speed_calc = AppliedMath(speed_points) 
    speed_graph = speed_calc.create_graph()  
    print(speed_graph["coefficients"])






if __name__ == "__main__":
    main()
