__author__ = "Ashad Nadeem Mahmudi"
__date__ = "9/1/2020"

from PIL import Image
import os

folder = os.path.join(os.getcwd(),"BulkImages")

imgList = os.listdir(folder)

try:
    os.mkdir("../AutomatingRealLifeTasksWithPython/BulkImagesResult")
except FileExistsError:
    print("Directory Exists")

print(os.getcwd())

for imgs in imgList:
    if imgs.startswith("."):
        continue
    new_ext = imgs.split(".")[0] + ".jpg"
    print(imgs)
    im = Image.open(os.path.join(folder,imgs))
    im = im.convert('RGB')
    im = im.rotate(270)
    im = im.resize((128,128))
    directory = os.path.join("BulkImagesResult",new_ext)
    new_img = im.save(directory, format="JPEG")