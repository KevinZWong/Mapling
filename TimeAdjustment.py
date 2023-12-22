from tkinter import *
from tkSliderWidget import Slider

class SliderApp:
    def __init__(self, root, given_length_effect, given_points_list):
        self.root = root
        self.given_length_effect = given_length_effect
        self.given_points_list = given_points_list
        self.points_backup = given_points_list
        self.intervals_list = self.calculate_intervals()
        self.setup_slider()
        self.setup_label()
        # Button to finalize the points selection
        self.done_button = Button(root, text="Done", command=self.finalize_points)
        self.done_button.pack(side=RIGHT)

    def calculate_intervals(self):
        intervals_list = []
        intervals = 0
        for _ in range(len(self.given_points_list)):
            intervals += self.given_length_effect / (len(self.given_points_list) + 1)
            intervals_list.append(intervals)
        return intervals_list

    def setup_slider(self):
        self.slider = Slider(
            self.root,
            width=400,
            height=60,
            min_val=0,
            max_val=self.given_length_effect,
            init_lis=self.intervals_list,
            show_value=True,
            removable=True,
            addable=True
        )
        self.slider.setValueChageCallback(self.on_value_change)
        self.slider.pack()

    def setup_label(self):
        self.instructions = StringVar()
        self.label = Label(self.root, textvariable=self.instructions)
        self.instructions.set("Time interval between points")
        self.label.pack()

    def on_value_change(self, vals):
        pass

    def get_slider_values(self):
        return self.slider.getValues()
    def finalize_points(self):
        # If there's any action to be taken when points selection is done, it goes here.
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = SliderApp(root, 15, [(73, 368), (205, 496), (446, 632), (691, 683), (799, 587), (742, 434), (561, 433)])
    root.title("Slider Widget")
    root.mainloop()

    print(app.get_slider_values())
