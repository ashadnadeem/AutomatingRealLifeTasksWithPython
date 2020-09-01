__author__ = "Ashad Nadeem Mahmudi"
__date__ = "9/1/2020"

from PIL import Image

#Opening Image as im
im = Image.open("ImagesExample/example.jpg")

#Resizing
new_im = im.resize((640,480))
new_im.save("ImagesExample/example_resized.jpg")

#Rotating
new_im = im.rotate(90)
new_im.save("ImagesExample/example_rotated.jpg")

#Flipped and Resized
im.rotate(180).resize((640,480)).save("ImagesExample/flipped_and_resized.jpg")

#Change Format
print(im.format)

im = im.convert('RGB')
im.save("ImagesExample/new_format_image.jpg",format="JPEG")