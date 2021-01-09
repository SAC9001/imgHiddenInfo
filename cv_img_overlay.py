import cv2
import os
import shutil
import xml.etree.ElementTree as ET
import random

# 为防止出现对应xml文件不存在(即该图片没有标定框)的情况
# 读取文件名应从xml文件夹中读取

bg_folder = r'D:\Users\NPCD\Documents\Lab\temp\background'
img_folder = r'D:\Users\NPCD\Documents\Lab\temp\screen_236\images'
xml_folder = r'D:\Users\NPCD\Documents\Lab\temp\screen_236\xmls'
out_img_folder = r'D:\Users\NPCD\Documents\Lab\temp\overlay_img\screen\images'
out_xml_folder = r'D:\Users\NPCD\Documents\Lab\temp\overlay_img\screen\xmls'

if os.path.exists(out_img_folder):
    shutil.rmtree(out_img_folder)
os.makedirs(out_img_folder)
if os.path.exists(out_xml_folder):
    shutil.rmtree(out_xml_folder)
os.makedirs(out_xml_folder)


def single_img(img_name, bg_name):
    img = cv2.imread(img_folder + r'\%s.jpg' % img_name)
    xml_dir = xml_folder + r'\%s.xml' % img_name
    # bg_name = os.path.splitext(os.path.basename(bg_dir))
    bg_dir = '%s\%s' % (bg_folder, bg_name)
    bg_img = cv2.imread(bg_dir)
    bg_height = bg_img.shape[0]
    bg_width = bg_img.shape[1]

    # xml process part
    # get img info from xml
    xml = ET.parse(xml_dir)
    root = xml.getroot()
    xml_size = root.find('size')
    xml_bndbox = root.find('object').find('bndbox')

    # img process part
    # target img resize
    size_rate = 0.3
    img_sized = cv2.resize(img, None, fx=size_rate, fy=size_rate)
    
    # xml process part
    # calculate new xml info
    movable_height = bg_height - img_sized.shape[0]
    movable_width = bg_width - img_sized.shape[1]

    anchor_height = random.randint(1, movable_height)
    anchor_width = random.randint(1, movable_width)

    new_bndbox_xmin = int(float(xml_bndbox.find('xmin').text) * size_rate) + anchor_width
    new_bndbox_xmax = int(float(xml_bndbox.find('xmax').text) * size_rate) + anchor_width
    new_bndbox_ymin = int(float(xml_bndbox.find('ymin').text) * size_rate) + anchor_height
    new_bndbox_ymax = int(float(xml_bndbox.find('ymax').text) * size_rate) + anchor_height

    new_size_width = bg_width
    new_size_height = bg_height

    # img process
    # add img to bg
    # store new bg
    bg_img[anchor_height:anchor_height + img_sized.shape[0], 
    anchor_width:anchor_width + img_sized.shape[1]] = img_sized
    # cv2.imshow('final result', bg_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    out_name_main = r'%s_in_%s' % (img_name, os.path.splitext(bg_name)[0])
    out_img_dir = out_img_folder + r'\%s.jpg' % out_name_main
    cv2.imwrite(out_img_dir, bg_img)

    # xml process part
    # store new xml
    xml_size.find('width').text = str(bg_width)
    xml_size.find('height').text = str(bg_height)
    xml_bndbox.find('xmin').text = str(new_bndbox_xmin)
    xml_bndbox.find('xmax').text = str(new_bndbox_xmax)
    xml_bndbox.find('ymin').text = str(new_bndbox_ymin)
    xml_bndbox.find('ymax').text = str(new_bndbox_ymax)
    out_xml_dir = r'%s\%s.xml' % (out_xml_folder, out_name_main)
    xml.write(out_xml_dir)

for bg_name in os.listdir(bg_folder):
    print(r'background pic :  ' + bg_name)
    for name in os.listdir(xml_folder):
        name_main = os.path.splitext(name)[0]
        single_img(name_main, bg_name)
    