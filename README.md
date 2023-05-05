# OVERVIEW
This is a Python script that sorts files into various folders based on their file extension. The script will move files to specific folders such as documents, photos, videos, screenshots, compressed files, sound files, and others.

# Prerequisites
Python 3.x installed
shutil, os modules installed



# How to use
Set the sort_need variable to the directory path where you want to sort the files.
Run the script.
The script will create folders for different file types and move files to their respective folders based on their file extension.



# Functions
The script has four functions:
checker(path) - checks if the given path exists, if it doesn't exist, creates the directory.

is_folder(folder) - checks if the given path is a folder or not.

is_screenshot(name) - checks if the given file name contains the word "Screenshot" or not.

mover(file_location, where) - moves the file to the specified folder.



# File Types
Documents: pdf, docx, doc, txt, rtf, odt, pptx, ppt, xls, xlsx, csv
Videos: mp4, mov, avi, wmv, mkv, flv, m4v, webm
Photos: jpg, jpeg, png, gif, bmp, tiff, webp, raw
Compressed Files: zip, tar, gz, bz2, xz, 7z, rar
Sound Files: mp3, wav, flac, m4a, aac, ogg, wma
Screenshots: files containing the word "Screenshot" in their name
Others: files that don't fall into any of the above categories
