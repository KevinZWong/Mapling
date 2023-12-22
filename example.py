
import easygui
from moviepy.editor import ImageClip
import os
from DynamicEffects import DynamicPositionClip
from Spline3D import Spline3D
import cv2
import os

frame_rate = 60
clip_duration = 7
resolution = "1080x1920"
video_name = "test2"
image_path = "images/corgi.jpg"
movement_file = "mapling_models/spline_data_loop.json"
save_folder = "finishedVideos"
upscale = 1.5 # the size of image us upscaled until atleast 1.5 times greater than frame size

bg_width, bg_height = map(int, resolution.split("x"))
output_path = os.path.join(save_folder, video_name + ".mp4")
clip = ImageClip(image_path)
width, height = clip.size

max_final_res = max(bg_height, bg_width) * upscale

if width < height:
    new_height = int(max_final_res)
    new_width = int(width/height * max_final_res)
else:
    new_height = int(height/width * max_final_res)
    new_width = int(max_final_res)
bg_height

img = cv2.imread(image_path)
img_resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)


image_temp = "temp.jpg"
cv2.imwrite(image_temp, img_resized)

dynamic_clip = DynamicPositionClip(frame_rate, bg_width, bg_height)
movement_model = Spline3D()
movement_model.load_data(movement_file)
composite = dynamic_clip.generate_video(image_temp, clip_duration, movement_model)
composite.write_videofile(output_path, fps=frame_rate)
os.remove(image_temp)

