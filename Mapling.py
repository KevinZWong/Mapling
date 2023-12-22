
import easygui
from moviepy.editor import ImageClip
import os
from DynamicEffects import DynamicPositionClip
from Spline3D import Spline3D
import cv2
import os
field_names = ["Frame Rate (60)", "Clip Duration (10)", "Resolution (1080x1920)", "Video Name", "Upscale Factor (1.5)"]
field_values = []  
field_values = easygui.multenterbox("Enter the following values:", "Video Settings", field_names)

if '' in field_values:
    print("Error: Atleat one text box empty")
    exit()

frame_rate, clip_duration, resolution, video_name , upscale= field_values
frame_rate = int(frame_rate)
clip_duration = int(clip_duration)
upscale = float(upscale)
bg_width, bg_height = map(int, resolution.split("x"))

image_path = easygui.fileopenbox(msg="Select an image file:", title="Select Image", filetypes=["*.jpg", "*.jpeg", "*.png"])
model_file = easygui.fileopenbox(msg="Select a Mapling Model file:", title="Select Model", filetypes=["*.json"])
save_folder = easygui.diropenbox(msg="Select a folder to save the finished video:", title="Select Save Folder")

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
movement_model.load_data(model_file)
composite = dynamic_clip.generate_video(image_temp, clip_duration, movement_model)
composite.write_videofile(output_path, fps=frame_rate)
os.remove(image_temp)

