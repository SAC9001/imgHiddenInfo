import os
import shutil
import xml.etree.ElementTree as ET
import pickle

classes = ['IDcard']

xml_folder = r'D:\Users\NPCD\Documents\Lab\temp\IDcard_67\xml'
txt_folder = r'D:\Users\NPCD\Documents\Lab\temp\IDcard_67\labels'
# xml_folder = r'D:\Users\NPCD\Documents\Lab\temp\screen_236\screen_xml_rotate_90'
# txt_folder = r'D:\Users\NPCD\Documents\Lab\temp\screen_236\screen_txt_rotate_90'
# xml_folder = r'D:\Users\NPCD\Documents\Lab\temp\screen_236\screen_xml_rotate_180'
# txt_folder = r'D:\Users\NPCD\Documents\Lab\temp\screen_236\screen_txt_rotate_180'
# xml_folder = r'D:\Users\NPCD\Documents\Lab\temp\screen_236\screen_xml_rotate_270'
# txt_folder = r'D:\Users\NPCD\Documents\Lab\temp\screen_236\screen_txt_rotate_270'
# xml_folder = r'D:\Users\NPCD\Documents\Lab\temp\screen_236\screen_xml'
# txt_folder = r'D:\Users\NPCD\Documents\Lab\temp\screen_236\screen_txt'
if os.path.exists(txt_folder):
    shutil.rmtree(txt_folder)
os.makedirs(txt_folder)

def convert(size, box):
    dw = 1.0/size[0]
    dh = 1.0/size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]

    xx = x * dw
    yy = y * dh
    ww = w * dw
    hh = h * dh

    return (xx, yy, ww, hh)

def convert_annotation(image_name):
    inputFile = open(xml_folder + r'\%s.xml' % image_name, encoding='UTF-8')
    outputFile = open(txt_folder + r'\%s.txt' % image_name, 'w', encoding='UTF-8')

    tree = ET.parse(inputFile)
    root = tree.getroot()
    width = int(root.find('size').find('width').text)
    height = int(root.find('size').find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlBox = obj.find('bndbox')
        bndBox = (float(xmlBox.find('xmin').text), float(xmlBox.find('xmax').text),
                  float(xmlBox.find('ymin').text), float(xmlBox.find('ymax').text))
        bb = convert((width, height), bndBox)
        outputFile.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

for filename in os.listdir(xml_folder):
    PerFilename = os.path.splitext(filename)[0]
    print(os.path.splitext(filename)[0])
    convert_annotation(PerFilename)