import os
import collections
from pprint import pprint
from traceback import print_tb
#####################
print ("Holako M9ewd M9ewd M9ewd M9ewd M9ewd")
# extation
ex_compress =['iso','zip', 'tar', 'torrent', 'rar', '7z']
ex_document = ['txt', 'pdf', 'csv', 'xls', 'doc', 'docx', 'html','ppt', 'pptx']
ex_music = ['mp3','wav']
ex_program =['exe','msi']
ex_video =['mp4','avi','mkv','mov','mpg','h264']
ex_image =['png','jpg','jpeg','gif','ico','bmp','webp','PNG']

#main path
source_dir ="C:\\Users\\Administrator\\Downloads"
dest_dir_prog ="C:\\Users\\Administrator\\Downloads\\Programs"
dest_dir_music ="C:\\Users\\Administrator\\Downloads\\Music"
dest_dir_video ="C:\\Users\\Administrator\\Downloads\\Video"
dest_dir_image = "C:\\Users\\Administrator\\Downloads\\Images"
dest_dir_doc = "C:\\Users\\Administrator\\Downloads\\Documents"
dest_dir_comp = "C:\\Users\\Administrator\\Downloads\\Compressed"

# mapping filesL
files_mapping = collections.defaultdict(list)
files_list = os.listdir(source_dir)

for file_name in files_list:
    file_ext  = file_name.split('.')[-1]
    files_mapping[file_ext].append(file_name)

#move files 
for f_ext, f_list in files_mapping.items():

    if f_ext in ex_program:
        for file in f_list:
            os.rename(os.path.join(source_dir, file), os.path.join(dest_dir_prog, file))
        print (" all programs done")

    elif f_ext in ex_music:
        for file in f_list:
            os.rename(os.path.join(source_dir, file), os.path.join(dest_dir_music, file))
        print (" all music done")

    elif f_ext in ex_video:
        for file in f_list:
            os.rename(os.path.join(source_dir, file), os.path.join(dest_dir_video, file))
        print (" all vedios done")

    elif f_ext in ex_image:
        for file in f_list:
            os.rename(os.path.join(source_dir, file), os.path.join(dest_dir_image, file))
        print (" all images done")

    elif f_ext in ex_document:
        for file in f_list:
            os.rename(os.path.join(source_dir, file), os.path.join(dest_dir_doc, file))
        print (" all documents done")


    elif f_ext in ex_compress:
        for file in f_list:
            os.rename(os.path.join(source_dir, file), os.path.join(dest_dir_comp, file))
        print (" all compressed files done")

 