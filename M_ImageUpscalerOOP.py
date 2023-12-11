import cv2
from cv2 import dnn_superres
#pip install opencv-contrib-python
from PIL import Image
class ImageSuperResolution:
    def __init__(self):
        self.sr = dnn_superres.DnnSuperResImpl_create()
        self.modelPath = "models/LapSRN_x2.pb"
        self.modelName = "lapsrn"
        #"/model/LapSRN_x8.pb"
        #"/model/LapSRN_x.pb"
        #"/model/LapSRN_x8.pb"


    def read_model(self, model_path, model_name, scale):
        self.sr.readModel(model_path)
        self.sr.setModel(model_name, scale)

    def upscale(self, image_path):
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Image at {image_path} could not be read.")
        return self.sr.upsample(image)

    def save_image(self, image, output_path):
        cv2.imwrite(output_path, image)

    def process_image(self, scale, image_path, output_path):
        self.read_model(self.modelPath, self.modelName, scale)
        result = self.upscale(image_path)
        self.save_image(result, output_path)
    def convert_webp_to_jpg(self, input_image_path, output_image_path):

        try:
            # Open the WebP image file
            with Image.open(input_image_path) as image:
                # Convert the image to RGB mode (if not already in this mode)
                rgb_image = image.convert('RGB')
                # Save the image in JPG format
                rgb_image.save(output_image_path, 'JPEG')
            print(f"Conversion successful. Image saved as '{output_image_path}'")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    model_path = "/models/LapSRN_x2.pb"
    model_name = "lapsrn"
    scale = 2
    #raw_path = "/home/kevin/Desktop/PARSE/Mapling/images/corgi.webp"
    image_path = "/home/kevin/Desktop/PARSE/Mapling/images/corgi.jpg"
    output_path = "/home/kevin/Desktop/PARSE/Mapling/upscaled/upscaledcorgi3.jpg"
    
    isr = ImageSuperResolution()
    #isr.convert_webp_to_jpg(raw_path, image_path)
    isr.process_image(scale, image_path, output_path)



