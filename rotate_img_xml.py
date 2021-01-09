import os
import xml.etree.ElementTree as ET
import shutil
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

origin_img_folder = r'D:\Users\NPCD\Documents\Lab\temp\IDcard_67\IDcard_img'
origin_xml_folder = r'D:\Users\NPCD\Documents\Lab\temp\IDcard_67\IDcard_xml'

out_img_rotate90_folder = r'D:\Users\NPCD\Documents\Lab\temp\IDcard_67\IDcard_img_rotate_90'
if os.path.exists(out_img_rotate90_folder):
    shutil.rmtree(out_img_rotate90_folder)
os.makedirs(out_img_rotate90_folder)

out_img_rotate180_folder = r'D:\Users\NPCD\Documents\Lab\temp\IDcard_67\IDcard_img_rotate_180'
if os.path.exists(out_img_rotate180_folder):
    shutil.rmtree(out_img_rotate180_folder)   
os.makedirs(out_img_rotate180_folder)

out_img_rotate270_folder = r'D:\Users\NPCD\Documents\Lab\temp\IDcard_67\IDcard_img_rotate_270'
if os.path.exists(out_img_rotate270_folder):
    shutil.rmtree(out_img_rotate270_folder)   
os.makedirs(out_img_rotate270_folder)

out_xml_rotate90_folder = r'D:\Users\NPCD\Documents\Lab\temp\IDcard_67\IDcard_xml_rotate_90'
if os.path.exists(out_xml_rotate90_folder):
    shutil.rmtree(out_xml_rotate90_folder)
os.makedirs(out_xml_rotate90_folder)

out_xml_rotate180_folder = r'D:\Users\NPCD\Documents\Lab\temp\IDcard_67\IDcard_xml_rotate_180'
if os.path.exists(out_xml_rotate180_folder):
    shutil.rmtree(out_xml_rotate180_folder)   
os.makedirs(out_xml_rotate180_folder)

out_xml_rotate270_folder = r'D:\Users\NPCD\Documents\Lab\temp\IDcard_67\IDcard_xml_rotate_270'
if os.path.exists(out_xml_rotate270_folder):
    shutil.rmtree(out_xml_rotate270_folder)   
os.makedirs(out_xml_rotate270_folder)

def Coordinate_rotate_90(width, height, xmin, xmax, ymin, ymax):
    xxmin = ymin
    xxmax = ymax
    yymin = str(int(float(width) - float(xmax)))
    yymax = str(int(float(width) - float(xmin)))
    return xxmin, xxmax, yymin, yymax

def Coordinate_rotate_180(width, height, xmin, xmax, ymin, ymax):
    xxmin = str(int(float(width) - float(xmax)))
    xxmax = str(int(float(width) - float(xmin)))
    yymin = str(int(float(height) - float(ymax)))
    yymax = str(int(float(height) - float(ymin)))
    return xxmin, xxmax, yymin, yymax

def Coordinate_rotate_270(width, height, xmin, xmax, ymin, ymax):
    xxmin = str(int(float(height) - float(ymax)))
    xxmax = str(int(float(height) - float(ymin)))
    yymin = xmin
    yymax = xmax
    return xxmin, xxmax, yymin, yymax

def XmlProcess_90(name_main):
    xml_dir = origin_xml_folder + r'\%s.xml' % name_main
    tree = ET.parse(xml_dir)
    root = tree.getroot()
    size = root.find('size')
    bndbox = (root.find('object')).find('bndbox')

    width = size.find('width')
    height = size.find('height')

    xmin = bndbox.find('xmin')
    xmax = bndbox.find('xmax')
    ymin = bndbox.find('ymin')
    ymax = bndbox.find('ymax')

    xmin.text, xmax.text, ymin.text, ymax.text = Coordinate_rotate_90(width.text, height.text,
    xmin.text, xmax.text, ymin.text, ymax.text)

    temp = width.text
    width.text = height.text
    height.text = temp

    out_xml_rotate90_dir = out_xml_rotate90_folder + r'\%s_rotate_90.xml' % name_main
    tree.write(out_xml_rotate90_dir)
    print('xml saved: ' + out_xml_rotate90_dir)

def XmlProcess_180(name_main):
    xml_dir = origin_xml_folder + r'\%s.xml' % name_main
    tree = ET.parse(xml_dir)
    root = tree.getroot()
    size = root.find('size')
    bndbox = (root.find('object')).find('bndbox')

    width = size.find('width')
    height = size.find('height')

    xmin = bndbox.find('xmin')
    xmax = bndbox.find('xmax')
    ymin = bndbox.find('ymin')
    ymax = bndbox.find('ymax')

    xmin.text, xmax.text, ymin.text, ymax.text = Coordinate_rotate_180(width.text, height.text,
    xmin.text, xmax.text, ymin.text, ymax.text)

    # temp = width.text
    # width.text = height.text
    # height.text = temp

    out_xml_rotate180_dir = out_xml_rotate180_folder + r'\%s_rotate_180.xml' % name_main
    tree.write(out_xml_rotate180_dir)
    print('xml saved: ' + out_xml_rotate180_dir)

def XmlProcess_270(name_main):
    xml_dir = origin_xml_folder + r'\%s.xml' % name_main
    tree = ET.parse(xml_dir)
    root = tree.getroot()
    size = root.find('size')
    bndbox = (root.find('object')).find('bndbox')

    width = size.find('width')
    height = size.find('height')

    xmin = bndbox.find('xmin')
    xmax = bndbox.find('xmax')
    ymin = bndbox.find('ymin')
    ymax = bndbox.find('ymax')

    xmin.text, xmax.text, ymin.text, ymax.text = Coordinate_rotate_270(width.text, height.text,
    xmin.text, xmax.text, ymin.text, ymax.text)

    temp = width.text
    width.text = height.text
    height.text = temp

    out_xml_rotate270_dir = out_xml_rotate270_folder + r'\%s_rotate_270.xml' % name_main
    tree.write(out_xml_rotate270_dir)
    print('xml saved: ' + out_xml_rotate270_dir)


def Img_Process_90(img_dir, name_main, name_type):
    img = Image.open(img_dir)
    img = img.transpose(Image.ROTATE_90)
    save_dir = out_img_rotate90_folder + r'\%s_rotate_90%s' % (name_main, name_type)
    img.save(save_dir)
    print('image saved: ' + save_dir)
    XmlProcess_90(name_main)

def Img_Process_180(img_dir, name_main, name_type):
    img = Image.open(img_dir)
    img = img.transpose(Image.ROTATE_180)
    save_dir = out_img_rotate180_folder + r'\%s_rotate_180%s' % (name_main, name_type)
    img.save(save_dir)
    print('image saved: ' + save_dir)
    XmlProcess_180(name_main)

def Img_Process_270(img_dir, name_main, name_type):
    img = Image.open(img_dir)
    img = img.transpose(Image.ROTATE_270)
    save_dir = out_img_rotate270_folder + r'\%s_rotate_270%s' % (name_main, name_type)
    img.save(save_dir)
    print('image saved: ' + save_dir)
    XmlProcess_270(name_main)

def Img_Process(img_dir, name_main, name_type):
    Img_Process_90(img_dir, name_main, name_type)
    Img_Process_180(img_dir, name_main, name_type)
    Img_Process_270(img_dir, name_main, name_type)

for img_name_full in os.listdir(origin_img_folder):
    this_img_dir = origin_img_folder + r'\%s' % img_name_full
    img_name_main = os.path.splitext(img_name_full)[0]
    img_name_type = os.path.splitext(img_name_full)[1]
    print('dealing with ' + this_img_dir)
    Img_Process(this_img_dir, img_name_main, img_name_type)
    