import os
import zipfile
from send2trash import send2trash

# WINDOWS 10
# dir_name = 'C:\\Users\Anonymous\\Downloads'
# unizped_files = 'C:\\Users\Anonymous\\Desktop\\Unziped_files'
# extension = ".zip"

# LINUX UBUNTU 20.04
dir_name = '/home/anonymous/Downloads'
unizped_files = '/home/anonymous/Desktop/Unziped_files'
extension = ".zip"

os.chdir(dir_name)  # change directory from working dir to dir with files

for item in os.listdir(dir_name):  # loop through items in dir
    if item.endswith(extension):  # check for ".zip" extension
        file_name = os.path.abspath(item)  # get full path of files
        zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
        zip_ref.extractall(unizped_files)  # extract file to dir
        zip_ref.close()  # close file
        # os.remove(file_name)  # delete zipped file
        send2trash(file_name)  # del and move to the trash


# AutoUnzip => tiny program to Unzip all files from marked folder(Downloads) to the desktop (Unziped_files) folder and Delete zip file to the trash/or permanently


# installation
# Copy script (zip.py) to the Downloads directory and make it hidden file.
# Add Downloads folder to your PATH, On Linux Add permanently.
# Add file execution option, Linux(chmod +x zip.py)
# Create alias, for example "unz" or do not !


# fire "AutoUnzip"
# 1) download the whatever.zip file from internet.
# 2) open terminal and hit "unz" or "zip.py"
# 3) your files are on the desktop in Unziped_files folder and whatever.zip file is waiting for you on the trash.
