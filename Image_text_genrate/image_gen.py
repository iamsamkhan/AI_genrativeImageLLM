#pip install clip-interrogator==0.6.0

from PIL import Image
import cv2
from clip_interrogator import config, Interrogator

image=Image.open("office-home-house-desk-159839").convert("RGB")
image
from traitlets.traitlets import Integer
ci= Interrogator(config(clip_model_name="ViT-L-14/openai"))

result=ci.interrogate(image)
print(image)

