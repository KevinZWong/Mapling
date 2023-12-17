<<<<<<< HEAD
=======

from tkinter import *
from createGraph import AppliedMath
<<<<<<< HEAD



def main():
  
=======
from timeAdjustment import SliderApp
from pointSelection import PointSelectionApp
def main():

>>>>>>> 1429cb1 (update mapling)
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


    input("Please select points that represent speed of image across path (Press enter to continue): ")
    root = Tk()
    app = SliderApp(root, 15, [(73, 368), (205, 496), (446, 632), (691, 683), (799, 587), (742, 434), (561, 433)])
    root.title("Slider Widget")
    root.mainloop()

    print(app.get_slider_values())
'''
    ######## test ########

    path_points = [(69, 650), (155, 486), (331, 231), (426, 205), (455, 279), (418, 464), (371, 643)]
    speed_points = [(26, 660), (132, 459), (251, 275), (404, 238), (443, 349), (444, 443), (462, 637)]
    ######################
<<<<<<< HEAD
    '''
    
    
=======
>>>>>>> 1429cb1 (update mapling)
   
   
    path_calc = AppliedMath(path_points) 
    path_graph = path_calc.create_graph() 
    print(path_graph["coefficients"])
    
    speed_calc = AppliedMath(speed_points) 
    speed_graph = speed_calc.create_graph()  
    print(speed_graph["coefficients"])



'''


if __name__ == "__main__":
    main()
>>>>>>> 5c2d476 (update mapling)
