# Name: GatherFile - 1.0.0
# Author: Duc Van
# Date: 25/08/2020

import os
import shutil
from pathlib import Path 

#Define file extensions
EXT_DOCUMENT = ['.doc','.docx','.txt','.pdf']
EXT_IMG = ['.jpg','.jpeg','.png','.gif']
EXT_EXCEL = ['.xlsx','.xls']
EXT_PPT = ['.ppt','.pptx']
EXT_MUSIC = ['.mp3','.wave']
EXT_VID = ['.mp4','.avi','.mov','.mpeg']


# Move file to correct dir
for  fileNames in os.listdir(os.getcwd()):
    if os.path.isfile(fileNames) and fileNames not in ['GatherFile.py', 'GatherFile.exe']:
        #Check the file extension
        if Path(os.path.join(os.getcwd(), fileNames)).suffix.lower() in EXT_DOCUMENT:
            #Check if the folder exist or not, if not -> create a folder, then move file to the folder
            if not os.path.exists(os.path.join(os.getcwd(),'Documents')):
                os.makedirs('Documents')
                shutil.move(os.path.join(os.getcwd(), fileNames), os.path.join('Documents'))
            else:
                shutil.move(os.path.join(os.getcwd(), fileNames), os.path.join('Documents'))

        elif Path(os.path.join(os.getcwd(), fileNames)).suffix.lower() in EXT_IMG:
            if not os.path.exists(os.path.join(os.getcwd(),'Images')):
                os.makedirs('Images')
                shutil.move(os.path.join(os.getcwd(), fileNames), os.path.join('Images'))
            else:
                shutil.move(os.path.join(os.getcwd(), fileNames), os.path.join('Images'))

        elif Path(os.path.join(os.getcwd(), fileNames)).suffix.lower() in EXT_EXCEL:
            if not os.path.exists(os.path.join(os.getcwd(),'Excel')):
                os.makedirs('Excel')
                shutil.move(os.path.join(os.getcwd(), fileNames), os.path.join('Excel'))
            else:
                shutil.move(os.path.join(os.getcwd(), fileNames), os.path.join('Excel'))

        elif Path(os.path.join(os.getcwd(), fileNames)).suffix.lower() in EXT_PPT:
            if not os.path.exists(os.path.join(os.getcwd(),'Ppt')):
                os.makedirs('Ppt')
                shutil.move(os.path.join(os.getcwd(), fileNames), os.path.join('Ppt'))
            else:
                shutil.move(os.path.join(os.getcwd(), fileNames), os.path.join('Ppt'))

        elif Path(os.path.join(os.getcwd(), fileNames)).suffix.lower() in EXT_VID:
            if not os.path.exists(os.path.join(os.getcwd(),'Videos')):
                os.makedirs('Videos')
                shutil.move(os.path.join(os.getcwd(), fileNames), os.path.join('Videos'))
            else:
                shutil.move(os.path.join(os.getcwd(), fileNames), os.path.join('Videos'))

        elif Path(os.path.join(os.getcwd(), fileNames)).suffix.lower() in EXT_MUSIC:
            if not os.path.exists(os.path.join(os.getcwd(),'Musics')):
                os.makedirs('Musics')
                shutil.move(os.path.join(os.getcwd(), fileNames), os.path.join('Musics'))
            else:
                shutil.move(os.path.join(os.getcwd(), fileNames), os.path.join('Musics'))

        else:
            if not os.path.exists(os.path.join(os.getcwd(),'Others')):
                os.makedirs('Others')
                shutil.move(os.path.join(os.getcwd(), fileNames), os.path.join('Others'))
            else:
                shutil.move(os.path.join(os.getcwd(), fileNames), os.path.join('Others'))

print('All done !!!')
