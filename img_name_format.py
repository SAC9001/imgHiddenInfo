import os
import shutil

img_folder = r''
xml_folder = r''

img_count = 1

for xml_name_full in os.listdir(img_folder):
    name_main = os.path.splitext(xml_name_full)[0]
    img_name_old = img_folder + r'\%s.jpg' % name_main
    xml_name_old = xml_folder + r'\%s.xml' % name_main
    name_str = r'IMG_IDCard_' + r'%06d' % img_count
    img_name_new = img_folder + r'\%s.jpg' % name_str
    xml_name_new = xml_folder + r'\%s.xml' % name_str
    os.rename(img_name_old, img_name_new)
    if os.path.exists(xml_name_old):
        os.rename(xml_name_old, xml_name_new)
    print(img_name_old + r' -------> ' + img_name_new + r'\t' + 
    xml_name_old + r' =======> ' + xml_name_new)
    img_count += 1
