import os
import collections
#####################
# extation
ex_compress =['iso','zip', 'tar', 'torrent', 'rar', '7z']
ex_document = ['txt', 'pdf', 'csv', 'xls', 'doc', 'docx', 'html','ppt', 'pptx']
ex_music = ['mp3','wav']
ex_program =['exe','msi','apk']
ex_video =['mp4','avi','mkv','mov','mpg','h264']
ex_image =['png','jpg','jpeg','gif','ico','bmp','webp','PNG']

#main path
base_path = os.path.expanduser('~')
downloads_path = os.path.join(base_path, 'Downloads')
dest_dirs = [ 'Programs','Documents','Music','Video','Images','Compressed','Others']

for d in dest_dirs:
    dir_path = os.path.join(downloads_path, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
        
# mapping files
files_mapping = collections.defaultdict(list)
files_list = os.listdir(downloads_path)

for file_name in files_list:
    file_ext  = file_name.split('.')[-1]
    files_mapping[file_ext].append(file_name)

#move files 
for f_ext, f_list in files_mapping.items():
    if f_ext in ex_program:
        for file in f_list:
            os.rename(os.path.join(downloads_path, file), os.path.join(downloads_path, 'Programs',file))
        print (" all programs done")

    elif f_ext in ex_music:
        for file in f_list:
            os.rename(os.path.join(downloads_path, file), os.path.join(downloads_path,'Music', file))
        print (" all music done")

    elif f_ext in ex_video:
        for file in f_list:
            os.rename(os.path.join(downloads_path, file), os.path.join(downloads_path,'Video', file))
        print (" all vedios done")

    elif f_ext in ex_image:
        for file in f_list:
            os.rename(os.path.join(downloads_path, file), os.path.join(downloads_path,'Images', file))
        print (" all images done")

    elif f_ext in ex_document:
        for file in f_list:
            os.rename(os.path.join(downloads_path, file), os.path.join(downloads_path,'Documents',file))
        print (" all documents done")

    elif f_ext in ex_compress:
        for file in f_list:
            os.rename(os.path.join(downloads_path, file), os.path.join(downloads_path,'Compressed', file))
        print (" all compressed files done")
