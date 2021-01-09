import os
import shutil

txt_dir = r''
target_img_folder = r''
target_labels_folder = r''
if not os.path.exists(target_img_folder):
    shutil.rmtree(target_img_folder)
os.makedirs(target_img_folder)
if not os.path.exists(target_labels_folder):
    shutil.rmtree(target_labels_folder)
os.makedirs(target_labels_folder)

with open(txt_dir, 'r') as f:
    for line in f.readlines():
        img_origin_dir = line.strip('\n')
        img_name_main = os.path.splitext(os.path.basename(img_origin_dir))[0]
        label_dir = os.getcwd() + r'\labels\%s.xml' % img_name_main
        target_img_dir = target_img_folder + r'\%s.jpg' % img_name_main
        target_labels_dir = target_labels_folder + r'\%s.txt' % img_name_main
        # shutil.copy(img_origin_dir, target_dir)
        # shutil.copy(label_dir, target_labels_dir)
        print(img_origin_dir + ' ----------> ' + target_img_dir)
        print(label_dir + ' ----------> ' + target_labels_dir)