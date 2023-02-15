import os
import shutil

from_dir = 'C:/Users/HP/Downloads/LearnersWeb'
to_dir = 'C:/Users/HP/OneDrive/Documents'

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:

    name, ext = os.path.splitext(file)
    ext = ext[1:]
    
    path1 = from_dir + '/' + file
    path2 = to_dir + '/' 'Document Files' + '/' + file
    path3 = to_dir + '/' + "Document Files" + '/' + file
    
    if(ext == ''):
        continue
    
    if(os.path.exists(path2)):
        shutil.move(path1, path3)
    else:
        os.mkdir(path2)
        shutil.move(path1,path3)    
