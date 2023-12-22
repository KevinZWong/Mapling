from moviepy.editor import ImageClip, ColorClip, CompositeVideoClip
from Spline3D import Spline3D
class DynamicPositionClip:
    def __init__(self, framerate, bg_width, bg_height):
        self.framerate = framerate
        self.frame_width = bg_width
        self.frame_height = bg_height

    def dynamicPosition(self, t, movement_model, image_width, image_height, clip_duration):
        x_val, y_val = movement_model.get_x_y_for_z(t/(clip_duration/10))

        # Compute the maximum movement range considering the image size
        max_x_movement = self.frame_width - image_width
        max_y_movement = self.frame_height - image_height

        # Scale x, y values to fit within the frame boundaries
        # x_val and y_val range from 0 to 1000
        scaled_x = x_val / 1000 * max_x_movement
        scaled_y = y_val / 1000 * max_y_movement

        # Inverting the y to match the coordinate system (if necessary)
        return scaled_x, self.frame_height - scaled_y - image_height
   
    def generate_video(self, image_path, clip_duration, movement_model, output_path=None):
        clip = ImageClip(image_path).set_duration(clip_duration)
        image_width, image_height = clip.size
        bg_clip = ColorClip(size=(self.frame_width, self.frame_height), color=(0, 0, 0)).set_duration(clip_duration)
    
        # Use the passed-in movement_function to set the clip's position
        clip = clip.set_position(lambda t: self.dynamicPosition(t, movement_model, image_width, image_height, clip_duration))
        composite = CompositeVideoClip([bg_clip, clip])
        return composite
        

if __name__ == '__main__':
    FRAMERATE = 60

    clip_duration = 10
    image_path = "/home/kevin/Desktop/PARSE/Mapling/upscaled/upscaledcorgi3.jpg"
    output_path = "test8.mp4"
    bg_width = 1080
    bg_height = 1920
    dynamic_clip = DynamicPositionClip(FRAMERATE, bg_width, bg_height)
    movement_file = "spline_data_hook.json"
    movement_model = Spline3D()
    movement_model.load_data(movement_file)
    composite = dynamic_clip.generate_video(image_path, clip_duration, movement_model)
    composite.write_videofile(output_path, fps=FRAMERATE)