import os
from PIL import Image
import xml.etree.ElementTree as ET

# 图片的路径
dirs = r''
# xml文件的路径
xml_folder = r''

for filename in os.listdir(dirs):
    truedir = dirs + r'\\'
    truename = os.path.splitext(filename)[0]
    truend = os.path.splitext(filename)[1]
    print(truedir + filename)
    img = Image.open(truedir + filename)
    img = img.transpose(Image.ROTATE_90)
    img.save(truedir + truename + '_rotate_90' + truend)
    print(truedir + truename + '_rotate_90' + truend)
