# Mapling
A video animator tool that turns images into videos with custom pan movements.

## Example (Click)
[![Mapling Example](https://github.com/KevinZWong/Mapling/blob/main/images/corgi.jpg)](https://youtube.com/shorts/YtoLPY6lriI?feature=share)

## Summary
Mapling takes an image and upscales it until it is 150% larger than the resolution of the resulting video. It moves the image to a new position 60 times per second to create a video. The image's new position is determined by a customizable 3D spline graph that graphs x, y, and time into a single smooth curve. Points can be set to create your own custom curve (path of travel) for the image. The time between each point can be set to determine the speed of the image at any point. Everything is 100% customizable to create your very own custom image movement.  
## Usage

### **Pre-requisites:**
- **Pip**
- **Python 3.7+**
- **Virtual Environment** (highly recommended)

### **Installation:**
1. Clone the repository:   
`git clone https://github.com/KevinZWong/Mapling.git`  
`cd Mapling`  
`pip install -r requirements.txt`  
Run the examples.py which will create a second video named test2.mp4 for you to enjoy in the finishedVideos folder

### **Running the Example:**
- Run the `examples.py` which will create a second video named `test2.mp4` in the `finishedVideos` folder.

## Creating Custom Movement Paths

1. **Run the PathCreator.py Program:**
   - Execute `PathCreator.py`.
   - Follow the instructions provided on the command line.

2. **Using the GUI for Path Selection:**
   - After pressing enter, a GUI will appear.
   - Select the desired path for the image movement. Sides and corners represent the movement boundaries.
   - *Example:* For a curved movement path, arrange the points accordingly.
     ![GUI1]([https://github.com/KevinZWong/Mapling/blob/main/images/guild_gui1.png])

3. **Finalizing the Path:**
   - Click `Done`.
   - The next GUI allows adjustment of time intervals between selected points. Shorter intervals mean faster camera movement.
   - *Example:* For acceleration towards the end, arrange the points closer towards the end.
     ![GUI2]([[https://github.com/KevinZWong/Mapling/blob/main/images/guild_gui2.png])

4. **3D Model Preview:**
   - A 3D model representing the camera positions over time (x-position, y-position, time) will be displayed.
   - Close the graph when done.
     ![GUI2]([[https://github.com/KevinZWong/Mapling/blob/main/images/guild_gui3.png])
5. **Saving the Model:**
   - Follow the command line instructions to name your model.
   - Models are saved in the `mapling_models` folder.

## Using a Custom Mapling Model

1. **Run Mapling.py:**
   - Execute `Mapling.py`.

2. **Set Video Parameters via GUI:**
   - Input the following:
     - Framerate: Frames per second of the final video.
     - Clip Duration: Length of the final video.
     - Resolution: Width and height of the final video.
     - Video Name: Name of the final video (stored in `finishedVideos` folder).
     - Upscale Factor: Adjusts room for image movement. Higher values require more RAM. Values below 1 may cause black bars.

3. **Selecting Image and Model:**
   - Choose the image to animate.
   - Select the Mapling model from `mapling_models` folder.

4. **Finalize and Save:**
   - Choose the destination folder (`finishedVideos`) for the finished video.
